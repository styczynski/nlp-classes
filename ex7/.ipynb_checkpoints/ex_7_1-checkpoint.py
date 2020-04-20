from nltk.corpus import wordnet as wn
import nltk
import os
nltk.download('maxent_ne_chunker')
nltk.download('universal_tagset')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

rf = lambda v: str(round(v, 4))

corpus = nltk.corpus.rte.pairs(os.path.join(os.path.abspath(''), 'data/dev.xml'))

flatten_rte = lambda tags: enumerate(nltk.chunk.util.tree2conlltags(tags))

#
# Creates a list of objects with fields fromlists of RTE tags, text tokens and pos tags:
#   from - starting index of sequence
#   to - ending index of a sequence
#   text - text contents of the sequence
#   ne - NONE if the sequence is not an named entity / valid NE category otherwise
#
def clean_rte(rte_tags, tokens, pos_tags):
    flat_tags = flatten_rte(rte_tags)
    ents = []
    last_iob_tag = 'O'
    # Go through the IOB tagged tokens for the sentence
    for index, t in flat_tags:
        # Split IOB tag by "-"
        iob_tags = t[2].split('-')
        if iob_tags[0] != 'O':
            new_label = iob_tags[len(iob_tags)-1]
            # Rewrite the tags to match tags used by Spacy
            if new_label == "ORGANIZATION":
                new_label = "ORG"
            
            if iob_tags[0] == 'I' and last_iob_tag == 'B':
                # Continue last tag
                last_span = ents[len(ents)-1]
                ents[len(ents)-1] = {
                    "from": last_span["from"],
                    "to": last_span["to"]+1,
                    "ne": new_label,
                    "text": " ".join(tokens[last_span["from"]:last_span["to"]+1]),
                    "tag": t[1],
                }
            else:
                # Begin new tag
                ents.append({
                    "from": index,
                    "to": index+1,
                    "ne": new_label,
                    "text": tokens[index],
                    "tag": t[1],
                })
        last_iob_tag = iob_tags[0]
    all_ents = []
    cur_ne = 0
    token_index = 0
    while token_index < len(tokens):
        if cur_ne < len(ents):
            if ents[cur_ne]["from"] == token_index:
                all_ents.append(ents[cur_ne])
                token_index = ents[cur_ne]["to"]+1
                cur_ne = cur_ne+1
                continue
        all_ents.append({
            "from": token_index,
            "to": token_index+1,
            "ne": "NONE",
            "text": tokens[token_index],
            "tag": pos_tags[token_index][1],
        })
        token_index = token_index+1
    return all_ents
            
# Store all words to print only unique ones
all_words = set()

# Store output data
# Each line contains the tuple of
# - token contents
# - POS tag
# - synonyms
# - hypernyms
# - entire synsets list
lookup_data = []

# Go through all pairs in the corpus
for i, pair in enumerate(corpus):
    # Go through text and hyp from the pair
    for field in ['text', 'hyp']:
        input_text = pair.text
        if field == 'hyp':
            input_text = pair.hyp
        
        # Tokenize the text and filter out all characters
        tokens_text = [word for word in nltk.word_tokenize(input_text) if word.isalnum()]
        
        # POS-tagging
        pos_text = nltk.pos_tag(tokens_text, tagset='universal')
        
        # NER-tagging
        tags_text = nltk.ne_chunk(nltk.pos_tag(tokens_text))
        
        # Cleanup the NLTK NER fromat to most usable form
        text = clean_rte(tags_text, tokens_text, pos_text)
        
        # Iterate through all sequences
        for token in text:
            token_synonyms = []
            token_hypernyms = []
            # If the sequence is not a named entity
            if token["ne"] == "NONE":
                # Check if the word was already printed
                if f"{token['text']}-{token['tag']}" not in all_words:
                    all_words.add(f"{token['text']}-{token['tag']}")
                    # If not then check all the synsets
                    pos = None
                    synsets = wn.synsets(token["text"], pos=pos)
                    for syn in synsets:
                        for lem in syn.lemmas():
                            # Print lemmas for all the synonyms
                            token_synonyms.append(lem.name())
                        for hyp in syn.hypernyms():
                            # Print all hypernyms
                            token_hypernyms.append(hyp.name())
                    lookup_data.append((token['text'], token['tag'], token_synonyms, token_hypernyms, synsets))
                                  
# Print output in the requested format
# Format:
#
# <token> <pos_tag>
# <synonyms_comma_separated> <hypernims_comma_separated>
#
for token in lookup_data:
    print(f"{token[0]}\t{token[1]}\n{','.join(token[2])}\t{','.join(token[3])}")
    