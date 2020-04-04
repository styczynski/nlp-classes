from nltk.ccg import chart, lexicon
lex = lexicon.parseLexicon('''
:- S,N,NP,PP,VP

Det :: NP/N
Pro :: NP

I => Pro
shot => (S\\NP)/NP
an => Det
elephant => N
in => (NP\\NP)/NP
in => (S\\S)/NP
my => Det
pajamas => N
''')
parser = chart.CCGChartParser(lex, chart.DefaultRuleSet)
for parse in parser.parse("I shot an elephant in my pajamas".split()):
    chart.printCCGDerivation(parse)
