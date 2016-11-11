# Part II: Automata

REs and automata (both deterministic and nondeterministic!) are "the same thing". They look different on the surface level[1], but can express exactly the same _languages_, where "language" means "set of strings".
For instance, the automaton `→①-a→⓶↺ₐ` and the RE `a+` describe the language `{a, aa, aa, aaa, ...}`. So this particular RE and this particular automaton are equivalent to each other. 

Moreover, there is a corresponding automaton for any RE; and a corresponding RE for any automaton. Hence REs and automata, as *systems*, are equivalent.



## What is this useful for?

### Matching strings 
If you as a user just want to match some strings, writing REs is the common way to make standard tools understand what you want to match. [Here](https://regex101.com/), go match until your fingers are sore! ^_^

As for theory, it's useful to understand some limitations[2] of regular expressions -- for instance, you cannot match a string "an arbitrary amount of `a`s followed by *the same amount* of `b`s" with a regular expressions, no matter how clever RE you write. (Of course, you can do five 0s followed by five 1s, or fifty, but the keyword here is *arbitrary* same amount.)
Maybe looking at automata makes it clearer why some languages are not regular? Automata have no history; if you are in one state, you can take any transition from it, and you **cannot** restrict your automaton, like "go to state `q1` only if I got here with symbol *a*". 

A mandatory classic reading on the topic of limitations: [link](http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)


### Writing morphological analysers

If you are interested in developing morphological resources for some language, you'll need knowledge of morphological tools (lexc, twol, ...). With those tools, you can write *rewrite rules*, such as `n -> m / _ p` (*n* turns into *m* if followed by *p*), or parallel *constraints*, such as `n:m <=> _ b:p` (an *n* on the lexical side is realised as *m*, if it's followed by a *p* on the surface side, and that *p* is a *b* on the lexical side. Conversely, if there is a sequence *mp* on the surface side, then it must be an *nb* in the lexical side. This rule models two phenomena: first, the nasal assimilates in place of the plosive, and second, the plosive loses its voicing.) 

These tools use internally *transducers* to do all the fancy stuff. Transducers are like automata, but instead of just matching, they also transform the input.
As for theory, you as a user don't need much insight in automata/transducers, but more on the morphophonological phenomena that happen in your language. You just write local rules, what you need for each phenonemon, and all the fancy transducer magic transforms your rules into a single minimal black box that tackles all the morphology.


### Mathematical insight / writing tools to write morphological analysers

If you yourself want to write a better toolkit for writing morphological analysers, then you'll definitely need deep insight in the theory of finite-state automata and transducers.

Or if you're just interested in the pure mathematical sense, because you think that automata are beautiful. Well, then you'll likely feel that you *want* to have deep insight, less that you *need*.



## More resources

If you want to learn more about automata and formal languages:

* Chalmers course in LP4: http://www.cse.chalmers.se/edu/course/TMV027/ 

Related to NLP:

* Some history of the development of FST morphology: http://www.helsinki.fi/esslli/evening/20years.html
* Topics for the conference FSMNLP ("Finite-State Methods and Natural Language Processing"): [2015](http://fsmnlp2015.phil.hhu.de/?page_id=210), [2013](http://fsmnlp2013.cs.st-andrews.ac.uk/programme.html), [2012](http://ixa2.si.ehu.es/fsmnlp2012/index.php/en/programme.html)

## Footnotes 

[1] In fact, there are yet other ways to write down regular languages. Here's another notation: http://stackoverflow.com/questions/13816439/left-linear-and-right-linear-grammars/13945932#13945932 (probably you've seen it as a way to write context-free grammars).

[2] Perl-Compatible Regular Expressions (PCRE) have quite bit of extensions that exceed the power of regular languages. 
