# Part I: Introduction to NLP and overview of NLTK

## Question about printing Python objects

You were asked to do a frequency distribution by using `FreqDist` object in NLTK. Here's an example:

```python
>>> from nltk.book import text2
>>> from nltk import FreqDist
>>> fdist = FreqDist(text2)
```

In the interactive shell, we can just type the variable `fdist` and it will print some nice information. But if we try to call the `print()` function to it, this happens:

```python
>>> print(fdist)
<FreqDist with 6833 samples and 141576 outcomes>
```

The variable `fdist` is an object of the class `FreqDist`. 
Objects are complex structures, with many fields and methods. 
For FreqDist, these methods include `plot()`, for showing a nice graphical output, and `hapaxes()`, for printing out the words that only appear once.
In addition, there are a number of methods that all Python objects have. These include `__str__()` and `__repr__()`. (You can see that something fancy is going on because of the underscores!) Try it out:

```python
>>> fdist.__str__()
'<FreqDist with 6833 samples and 141576 outcomes>'
>>> fdist.__repr__()
"FreqDist({u',': 9397, u'to': 4063, u'.': 3975, u'the': 3861, u'of': 3565, u'and': 3350, u'her': 2436, u'a': 2043, u'I': 2004, u'in': 1904, ...})"
```

Actually they are so fancy that we can even write like this:

```python
>>> str(fdist)
'<FreqDist with 6833 samples and 141576 outcomes>'
>>> repr(fdist)
"FreqDist({u',': 9397, u'to': 4063, u'.': 3975, u'the': 3861, u'of': 3565, u'and': 3350, u'her': 2436, u'a': 2043, u'I': 2004, u'in': 1904, ...})"
```

The underscore-less functions cannot be written like that:

```python
>>> plot(fdist)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'plot' is not defined
```

So! What is the moral of this story? Let's get back to `print()`. We can call `print()` to any kinds of things, even if they are not strings: `print()` just implicitly calls the `__str__()` method of the object. In this case, `__repr__()` is actually the one with more interesting information. We can solve the problem by just calling repr before print (works outside shell too!):

```python
>>> print(repr(fdist))
FreqDist({u',': 9397, u'to': 4063, u'.': 3975, u'the': 3861, u'of': 3565, u'and': 3350, u'her': 2436, u'a': 2043, u'I': 2004, u'in': 1904, ...})
```

Or we can see if there is a special print method for the object using `dir(fdist)`.

## Built-in functions in Python

### dir()

You can find out information about specific variables or whole classes with the function `dir()`. For example:

```python
>>> dir(FreqDist)
['B', 'N', 'Nr', '__add__', '__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__missing__', '__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__unicode__', '__weakref__', '_cumulative_frequencies', 'clear', 'copy', 'elements', 'freq', 'fromkeys', 'get', 'hapaxes', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'max', 'most_common', 'plot', 'pop', 'popitem', 'pprint', 'r_Nr', 'setdefault', 'subtract', 'tabulate', 'unicode_repr', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
```
This will show you all methods for the `FreqDist` class. Also works if you type `dir(fdist)`: it will just give the same answer.

If you type `dir()` without arguments, it will show you everything you have in your namespace. 


```python
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
```

If you define your own variables or import something, `dir()` will show that too.

```python
>>> myList = [1,2,3]
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'myList']
>>> from nltk.book import *
>>> dir()
['FreqDist', 'Text', '__builtins__', '__doc__', '__name__', '__package__', 'babelize_shell', 'bigrams', 'genesis', 'gutenberg', 'inaugural', 'nps_chat', 'print_function', 'sent1', 'sent2', 'sent3', 'sent4', 'sent5', 'sent6', 'sent7', 'sent8', 'sent9', 'sents', 'text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9', 'texts', 'treebank', 'webtext', 'wordnet']
>>> dir(gutenberg)
['CorpusView', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_encoding', '_fileids', '_get_root', '_para_block_reader', '_read_para_block', '_read_sent_block', '_read_word_block', '_root', '_sent_tokenizer', '_tagset', '_unload', '_word_tokenizer', 'abspath', 'abspaths', 'encoding', 'ensure_loaded', 'fileids', 'open', 'paras', 'raw', 'readme', 'root', 'sents', 'unicode_repr', 'words']
```


### type()

You can query the types of variables. This works fine for

* primitive types: integer, boolean, ..

```python
>>> type(True)
<type 'bool'>
>>> type(3)
<type 'int'>
>>> type(3.14)
<type 'float'>
```

* collections: list, tuple, dict (though it doesn't tell you what is inside)

```python
>>> type((1,2,3))
<type 'tuple'>
>>> type([1,2,3])
<type 'list'>
>>> type({1:"foo",2:"bar"})
<type 'dict'>
```


* objects

```python
>>> type(fdist)
<class 'nltk.probability.FreqDist'>
```

You can query functions or classes, but the output isn't particularly helpful.

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


# Part III: Word statistics, language models and corpus methods

## PMI and LMI

### Logarithms

Doesn't matter which logarithm you use. They all preserve ranking: if `x > y`, then `log(x) > log(y)`.


### Transformation of the formula

The formula for PMI:

```
       p(x,y) 
log ____________
     p(x) * p(y)
```

Since `p(x)` is calculated as `count(x) / corpus_size`, we can present the formula also like this:


```
                count(x,y) / corpus_size 
log ____________________________________________
     (count(x)/corpus_size) * (count(y)/corpus_size)
```

which becomes


```
      (count(x,y) / corpus_size) * corpus_size * corpus_size
log __________________________________________________________
     count(x)               * count(y)
```

The `/ corpus_size` and one of the `* corpus_size`s cancel each other out, so we end up with

```
    count(x,y) * corpus_size
log ________________________
      count(x) * count(y)
```

Using this form of the formula, it is easier to show the following properties.


### Using and abusing PMI

PMI measures if two words are associated with each other, ie. if they occurr together in documents more often than they would "by change". (Possibly interesting side reading: [*Language is never, ever, ever random*](http://www.kilgarriff.co.uk/Publications/2005-K-lineer.pdf))
Bigger value for PMI = more related words.
As stated in the lecture and tutorial, PMI is biased towards rare words. Looking at the formula, there are two ways of getting a big number from the division:

* If `count(x,y)` is large
* If `count(x)` and/or `count(y)` is small

LMI, Lexicographers Mutual Information, is meant to balance this by multiplying the PMI result by `count(x,y)`.


Now let's think of some extreme scenarios.

#### 1. `count(x) ≈ count(y) ≈ count(x,y)`

In the first scenario, x and y appear only together, never alone.
We can subdivide this into the following cases:

##### 1a) `count(x) ≈ count(y) ≈ count(x,y) ≈ corpus_size`

The words `x` and `y` appear in almost every document. Let us assume there are only `p` documents where they don't appear. (If they appear in literally every document, what happens then?)
Think for instance `PMI(and, this)`.

```
     (corpus_size-p) * corpus_size               corpus_size
log ___________________________________ = log _________________ = log 1.000...1  ≈ 0.00...tiny number
     (corpus_size-p) * (corpus_size-p)         corpus_size - p
     
```

With LMI, we multiply the tiny number with the huge `corpus_size-p` number, and should get something not quite as tiny.

##### 1b) `count(x) ≈ count(y) ≈ count(x,y) ≈ 1`

The words `x` and `y` are rare on their own and hence rare together. 
For example, *sAiMZzqGdkpuJyWwIYMvZahVqVo* (I just decided that's the first word in my brand new conlang!) has one hit--this page--and *ἐκβουτῠπόομαι* has 192 hits.
(192 is totally ≈ 1 when we compare to the count for *the*. :-P)
This document is the only one that uses them together.
Then `PMI(sAiMZzqGdkpuJyWwIYMvZahVqVo, ἐκβουτῠπόομαι)` becomes

```
    1 * corpus_size
log ________________ = log corpus_size/192 = relatively big number
      1 * 192
```

With LMI, we multiply the relatively big number with the tiny `count(x,y)` and the number shouldn't change much.

#### 2. `count(x) ≈ corpus_size` and `count(y) ≈ count(x,y) ≈ 1`
 
One of the words is really common and the other is really infrequent. For instance, `PMI(those, ἐκβουτῠπόομαι)`.

```
       ~1 * corpus_size              corpus_size
log _____________________  = log  _________________
     (corpus_size-p) * ~1          corpus_size - p
```

PMI gives the same tiny number as the scenario `1a)`. But LMI shows the difference: here `count(x,y)` is tiny, and it won't change the tiny PMI into a bigger LMI.

So, the scenario *frequent x, frequent y, frequent x&y* gets a better LMI than *frequent x, infrequent y, infrequent x&y*. In contrast, both get the same PMI.

How does this scale down to the more common scenarios, with aardvarks, logarithms, googleology and science?

#### 3. `count(x) ≈ count(y) ≈ corpus_size` and `count(x,y) ≈ 1`

http://www.googlewhack.com/ was created to answer this question. 



