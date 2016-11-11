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
