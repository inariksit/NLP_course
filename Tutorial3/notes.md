# Tutorial 3

## Q1. (Toy) Brill tagger

Many of you did it by hand, not using `nltk.tag.brill`! No complaints about that ^^
If you want to see a toy version that actually uses the NLTK Brill, see [toy_brill.py](https://github.com/inariksit/NLP_course/blob/master/Tutorial3/toy_brill.py).


## Q2. Viterbi

All looked fine, except some forgot to add emission probabilities.

The sentence and the corpus was not so great for the task: there was only one possible path with any probability, others were just 0. 

Extra activities for interested (don't return them to me, just if you want to play around): 
 * Use a similar tiny corpus, apply smoothing
 * Calculate actual probabilities from some big corpus


## Q3. Uncertainty

Default tagger knows no uncertainty. Everything is a `<insert your favourite tag>`. It doesn't even need to look at the word to know that.

Lookup tagger is also very sure of itself. Unlike the default tagger, it looks at the word it tags. But its choice is always deterministic: for an ambiguous word, the most frequent is always correct. It doesn't want any extra information from the context. That'd just make the decision hard. :(

HMM acknowledges that the world is uncertain, and uses the context to determine the best choice. The candidates have different probabilities, and the most probable one is chosen.

Brill tagger has rules that change tag `A` to `B` in context `X __ Y`. But if it doesn't have a rule for a particular situation, then it goes with the default--could be lookup tagger, or even default tagger. (Or HMM tagger, or regexp tagger, or ...)

Constraint Grammar uses lists of tags. If it cannot disambiguate, it gives you a list of possible tags. "This *can* can be either NN or MD, I don't know which."

Finite-State Intersection Grammar uses disjunctions. "The tag sequence can be either `A-B-C` or `X-Y-C`, but not `A-Y-C` or `X-B-C`." This is stronger than Constraint Grammar, which says "first tag can be A or X, second tag can be B or Y, third can be only C".

Side reading: [*Part of Speech Tagging from a Logical Point of View*](http://www.ling.gu.se/~lager/Mutbl/Papers/lager_nivre.pdf)


## Q4. NLTK classifier

Looks fine! Relevant observations: 

* Rare words are more informative than frequent
* Emotional words can be misleading, "this film is shit/this film is the shit". Or what do the young people say nowadays.


## Q5. If you have a hammer...

Some general remarks

### Supervised/unsupervised

* Supervised: training data has labels
* Unsupervised: training data has no labels, algorithm tries to cluster similar items

*EXAMPLE*

### Distance measures

Distance measure means a way of measuring the difference between two (or more) items.

For instance, say we have bunch of strings and we want to measure their distance to the string “ABBA”. We decide to use the Levenshtein distance (usually called just “edit distance”): calculate the number of  single-character edits that is needed to change one word into the other.

1. “ABCA” - change C into B. Edit distance 1.
2. “BBBB” - change both B’s into A’s. Edit distance 2.
3. “HELP” - change all letters into A’s. Edit distance 4.
4. “HELPIAMTRAPPEDINCOMPUTATIONALLINGUISTICS” - edit distance is something very big, you need to delete almost every character.

Levenshtein distance is one distance measure we could use here. Another could be e.g. cosine similarity: we transform all the candidate strings into vectors which count how many times a character appears. 

So, ABBA would be 

```
  [A=2, B=2, C=0, D=0, …, Z=0] 
```
and without labels, this just becomes a vector of 26 values: `[1,1,0,0…,0]`.

Similarly, BBBB would be `[0,4,0,…,0]`.

Then we could map that into 26-dimensional space and calculate the cosine of the angle between the vectors. Spoiler: that measure is overkill for this task, but useful for some other tasks, where Levenshtein would be too simple.
(See this highly rated journal article for a better example: http://stackoverflow.com/a/1750187)

### Lexical selection

* Source word: *play*
* Labels: should we choose *leka* or *spela*?
* Features: e.g. is there a *piano* nearby? How about *doll*?

### Accent/diacritic restoration

* Source text: *kor*
* Classification task: is it actually *kor* or *kör*?
* Features: is there *mjölk* nearby? How about *bil*?

### Spam

Nice text from 2002: http://www.paulgraham.com/spam.html


### Q6. Entropy

```python
import nltk
import math

def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p * math.log(p,2) for p in probs)


a = ["spam", "spam", "spam"]
b = ["spam", "spam", "ham", "ham"]
c = ["horse", "giraffe", "horse", "aardvark", "kangaroo", "aardvark"]

names   = ["Max","Rex","Brutus","Lulu","Max","Bella","Max","Lulu"]
species = ["dog","dog","dog","dog","human","human","dog","human"]
n_s = list(zip(names, species))

for l in [a,b,c,n_s,names,species]:
  print(entropy(l))
```