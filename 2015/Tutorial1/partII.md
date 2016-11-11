# Part II: Automata

## Question: nondeterminism in parentheses

* `a` accepts _a_, and `a*` accepts 0 to infinite _a_'s.
* `ab` accepts _ab_, and `(ab)*` accepts 0 to infinite _ab_'s.

The expression in parentheses can also have some variation:

* `aba?` accepts _ab_ and _aba_. `(aba?)*` accepts any combinations of _ab_ and _aba_ in sequence, 0 to infinite times.

## Comments about automatic conversion between automata and regular expressions

Exercise 2.8 in Jurafsky & Martin was about manual conversion of automaton to regular expression (RE). 
There are several REs that describe the language of the automaton; the shortest and arguably the most human-readable is `(aba?)+`. 

A number of you gave a long and complex RE, which was not equivalent to the automaton, so I showed a way to construct even longer RE, with the plus side that it is equivalent to the automaton.
In case you're interested in the topic, the method I used was called *state removal method*. If you'd rather do formal semantics on your free time, the take-home message is "if you need to mess around with automata and RE, there are plenty of ways to make your computer do that for you".

**In this course, you're not expected to apply these methods. The following is just for your potential interest.**

### How is this useful?

As you've heard in class, REs and automata (both deterministic and nondeterministic!) are "the same thing". They look different on the surface level, but can express exactly the same _languages_, where "language" means "set of strings".
For instance, the automaton `→①-a→⓶↺ₐ` and the RE `a+` describe the language `{a, aa, aa, aaa, ...}`. This means that the particular RE and the particular automaton are equivalent to each other, and more broadly, REs and automata, as *systems*, are equivalent.

In addition to RE-automata equivalence, two or more REs and two or more automata can be equivalent to each other, such as the REs `a+` and `aa*`. There are then some natural questions to ask:

* Is the RE `(aba?)+` same as the RE `(ab|ab(aab)*(a|aab))+`?
* Is the RE `(aba?)+` same as the DFA *x*?
* Is the NFA *y* same as the NFA *z*?
* What is the smallest possible DFA for the RE `(aba?)+`?

In order to compare REs, it turns out that we need to go via automata. There is a unique, minimal deterministic automaton for each language, and we simply transform the REs/automata into that. When I say "simply", I mean the following steps:

* Convert your RE into an NFA: http://hackingoff.com/compilers/regular-expression-to-nfa-dfa
* Convert your ugly and verbose *nondeterministic* automaton into an ugly and verbose *deterministic* automaton: https://www.google.se/search?q=nfa+determinization
* Convert your ugly and verbose DFA into the unique, *minimal* DFA https://www.google.se/search?q=dfa+minimization


## More resources

If you want to learn more about automata:

* Chalmers course in LP4: http://www.cse.chalmers.se/edu/course/TMV027/ 
* Online course in Coursera, given at about LP1 (just ended for this year): https://www.coursera.org/course/automata

If you wonder what's the use for NLP:

* Spell checkers; anything related to morphology
* Topics for the conference FSMNLP ("Finite-State Methods and Natural Language Processing"): [2015](http://fsmnlp2015.phil.hhu.de/?page_id=210), [2013](http://fsmnlp2013.cs.st-andrews.ac.uk/programme.html), [2012](http://ixa2.si.ehu.es/fsmnlp2012/index.php/en/programme.html)
