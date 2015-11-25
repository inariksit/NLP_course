from nltk.tag       import DefaultTagger
from nltk.tbl.rule  import Rule
from nltk.tag.brill import BrillTagger, Pos


## Version 1: simple default tagger, nonsensical rules

nn_tagger = DefaultTagger('NN')       # Default tagger: tag everything as NN

# A dummy rule
rules = [Rule("01",                   # Number/ID of the rule
              "NN", "VB",             # Change NN to VB...
              [(Pos([0]), 'NN')])     # ...in context when the word is an NN 
        ]
my_brill = BrillTagger(nn_tagger, rules)


sentence = "can you can the can".split()
tagged = my_brill.tag(sentence)

print("Dummy Brill tagger:")
print(tagged)



## Version two, with a bit smarter default tagger & rules

from nltk.tag    import UnigramTagger
from nltk.corpus import brown

# Append to rules
newrules = [Rule("02",
                 "MD", "NN",           # Change MD to NN...
                 [(Pos([-1]), 'AT')])  # ...in context where there is an AT before
           ]

uni_tagger = UnigramTagger(brown.tagged_sents(categories='news')[:500])
my_slightly_smarter_brill = BrillTagger(uni_tagger, newrules)

tagged2 = my_slightly_smarter_brill.tag(sentence)
print("\nSlightly smarter Brill tagger:")
print(tagged2)
