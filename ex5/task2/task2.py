# !pip install nltk
import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
Nom -> N Nom | Adj Nom | Nom PP | N
NP -> Pro | Det Nom | Poss Nom
PP -> Prep NP
VP -> IntransV | TransV NP | IntransVwPP PP | VP PP
N -> 'elephant' | 'pajamas' | 'man' | 'telescope'
VP -> 'shot' | 'see' | 'saw'
IntransVwPP -> 'see' | 'saw'
TransV -> 'shot' | 'see' | 'saw'
IntransV -> 'shot'
VPto -> 'to' VP
Prep -> 'to' | 'in' | 'with'
Det -> 'an' | 'a'
Pro -> 'I'
Poss -> 'my'
""")

parser = nltk.ChartParser(grammar, trace=1)
text = "I saw a man with a telescope"
for tree in parser.parse(text.split(" ")):
    tree.draw()
    
