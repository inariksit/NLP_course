# Tutorial 3

## Q1. (Toy) Brill tagger

Many of you did it by hand, not using `nltk.tag.brill`! No complaints about that ^^
If you want to see a toy version that actually uses the NLTK Brill, see ___.


## Q2. Viterbi

All looked fine, except some forgot to add emission probabilities.

The sentence and the corpus was not so great for the task: there was only one possible path with any probability, others were just 0. 

Extra activities for interested (don't return them to me, just if you want to play around): 
 * Use a similar tiny corpus, apply smoothing
 * Calculate actual probabilities from some big corpus


## Q3. Uncertainty

Lookup tagger is very sure about itself: the most frequent is always correct. It doesn't even want any extra information, like context.

HMM acknowledges that the world is uncertain, and uses probabilities. 

Brill tagger wants to make an informed decision, and hence it looks at the context. "Oh, there is a determiner there, and I'm a verb--better go and change into a noun!" But if it doesn't find the information, then it goes with the default--could be lookup tagger ("can is MD, cause all the cans I've seen have been MDs!"), or even default tagger ("everything is NN. what do you mean other than NN exists?").

Constraint Grammar uses lists of tags. If it cannot disambiguate, it gives you a list of possible tags.

Finite-State Intersection Grammar is like "I can only tag in a perfect world where everything makes sense" and breaks if you throw any heuristics at it. But it does neat things with small amount of rules that don't contradict each other!

Side reading: "Part of Speech Tagging from a Logical Point of View" http://www.ling.gu.se/~lager/Mutbl/Papers/lager_nivre.pdf


## Q4. NLTK classifier

Looks fine! Relevant observations: 

* Rare words are more informative than frequent
* Emotional words can be misleading, "this film is shit/this film is the shit". Or what do the young people say nowadays.


## Q5. If you have a hammer...

Some general remarks

### Supervised/unsupervised/semi-supervised

### Distance measures


