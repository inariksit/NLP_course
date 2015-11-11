## Part I: Introduction to NLP and overview of NLTK

### Question about printing Python objects

You were asked to do a frequency distribution by using `FreqDist` object in NLTK. Here's an example (in a pan-Germanic language ^_^).

```python
>>> from nltk import FreqDist
>>> rawtext = "Kyllingen din er ikke trygg. Das ist kein Buch, sondern ein Mantel. Hoeveel landen zijn er in de wereld?"
>>> naive_split_text = rawtext.split()
```

The `split()` function takes a string and returns a list of strings.
If no parameter is given, it uses whitespace to split the sentence into words.
`naive_split_text` has the value `['Kyllingen', 'din', 'er', 'ikke', 'trygg.', 'Das', 'ist', 'kein', 'Buch,', 'sondern', 'ein', 'Mantel.', 'Hoeveel', 'landen', 'zijn', 'er', 'in', 'de', 'wereld?']`.

Now we create the frequency distribution to this particular text.

```python

```

### Built-in functions in Python

You can access

### type()

### dir()


## Part II: Automata

### Question: nondeterminism in parentheses

* `a` accepts _a_, and `a*` accepts 0 to infinite _a_'s.
* `ab` accepts _ab_, and `(ab)*` accepts 0 to infinite _ab_'s.

The expression in parentheses can also have some variation:

* `aba?` accepts _ab_ and _aba_. `(aba?)*` accepts any combination of _ab_ and _aba_ in sequence, 0 to infinite times.

### Comments about automatic conversion between FSA and regex

I showed in class a way to convert an automaton into a regular expression using the *state removal method*. 
This created a monstrous >20-character regular expression for something that can be expressed as `(aba?)+`.

How is this useful, and how do we know it's the same regular expression?

Regular expressions and automata are two different-looking ways of writing down _languages_, as in "sets of strings". 
The automaton `->①-ₐ->⓶` and the RE `a+` represent the language `{a, aa, aa, aaa...}`. We can also give it a human-language description: "infinitely many words containing _a_". 
The automaton and the RE just choose a different strategy to make the description more compact.


How do we see if `(TODO complex regex)` it's actually the same as `(aba?)+`? 



This course is an overview of many things, and isn't likely to go deeper into automata theory.
If some of you are interested to learn about the topic more deeply, I recommend a Chalmers course given in LP4: http://www.cse.chalmers.se/edu/course/TMV027/ . There is also an online course in Coursera, given at about LP1 (just ended for this year): https://www.coursera.org/course/automata

## Part III: Word statistics, language models and corpus methods

### PMI and LMI

Two things:

* Intuition about PMI and LMI
* Logarithms