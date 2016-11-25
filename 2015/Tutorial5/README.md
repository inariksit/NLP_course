# LT2113 H15 Natural language processing: Tutorial 5

General comment: There is absolutely no reason to apologise doing things in Python instead of calculating them on pen and paper! Programming, even just writing short and simple scripts, is an important skill which is going to save you a lot time later. It might be faster to count manually word frequencies of a tweet than write a function that does the same, but with the same function, you can also count the frequencies of a novel or a whole library.

TL;DR: It's great that you're doing things in Python, keep doing that!

## Q1, Q3-Q6.

If you have questions that I didn't answer in the individual feedback, do ask me! If I cannot answer you, I'll try at least to direct you to someone who knows more.


## Q2. Parsing: a summary

I enjoyed reading your answers! Some terms resulted in more confusion than others. I address common issues below, and individual feedback for more specific things.


### Generative grammar

There is a lot of association with Chomsky, or whether generative grammar is something that models how human brain works. 
Regardless of these questions, a generative grammar is simply a set of rules that generate all acceptable sequences in the language that the grammar describes.
Depending on the viewpoint, generative grammar can be contrasted with different things. A linguist could contrast a generative grammar with a formalism that allows more gradient view of language: utterances are not simply "yes" or "no", but there are degrees of acceptability. Another person would contrast generative grammar to a system that gives rules which forbid sequences (see Reductionist grammar).

A language described by a generative grammar doesn't have to be a natural language, it may well be a programming language. In addition, the grammar doesn't have to be a context-free grammar, it can be more or less expressive. Nor does it have to be necessarily a phrase-structure grammar.


### Dependency grammar vs. phrase-structure grammar

**Dependency grammar** is contrasted with a **phrase structure grammar** or **constituency grammar** (those two are more or less the same thing).

Dependency grammar will be happy if each word finds its head in the sentence. Word order doesn't matter. For instance, the sentences *I love you* and *you I love* have the same dependency tree. 

In contrast, phrase-structure grammar must first group words into constituents/subtrees/some kind of smaller units. On the simplest level, each word in itself is a constituent/subtree.
To return to the *I love you* / *You I love* example, the topicalisation will show in the parse in one way or another: a simple CFG could just have a rule `S -> NP NP VP` to account for the topicalised *you*. A more complex grammar could introduce transformations on some deep structure, and have all kinds of fancy nodes. In any case, the phrase structure of those two sentences is different.


#### Are phrase-structure grammar and constituency grammar synonyms?

So far I've just defined *constituency* as defined by the rules of the phrase-structure grammar. An S expanding to `NP NP VP` would be a constituent only because in this simple lazy grammar someone wrote such a rewrite rule. But constituency can also be defined using another method.

First we need to approach the problem from a dependency tree. There is a handy concept called [*catena*](http://taweb.aichi-u.ac.jp/tmgross/catena.html), which is defined as

>  a word or a combination of words that is continuous with respect to dominance.

Take the sentence "People like little dogs". The combination "like dogs" is a catena, since the omission of "little" doesn't break the dominance chain. But in order to be a constituent, it needs to be complete ("like dogs" is missing "little") and continuous ("like ... dogs" has a gap in the original string). In contrast, "like little dogs" is both a constituent and a catena.

For a full explanation, read this! http://taweb.aichi-u.ac.jp/tmgross/catena.html

### Reductionist grammar

Now onto something that is *not* generative!
A **reductionist** grammar formalism is constrasted with a **licencing** (or, *generative*!) grammar formalism. An empty reductionist grammar allows all possible strings in the world, whereas an empty licencing grammar allows no string.
[Constraint Grammar](http://beta.visl.sdu.dk/constraint_grammar.html) (CG) is an example of a reductionist system. The starting point is that the words can have any analysis provided by a morphological analyser, and the task of the constraint rules is to get rid of inappropriate analyses. A perfect CG leaves only the right POS tags (=more structure than we started with!), and an empty CG leaves in place all the POS tags.


### Expressivity

A couple of terms were related to the expressivity of the grammars: **regular grammar** and **context-free grammar**.
Many of you mentioned the [Chomsky hierarchy](https://en.wikipedia.org/wiki/Chomsky_hierarchy#Summary). Regular grammars are the least expressive, and context-free grammars come after regular grammars. You might find the numbering confusing (Type-0=most expressive, Type-3=least expressive)--don't worry about remembering a number, try to get an intuition about what kinds of production rules the grammars allow, what kinds of strings they accept and so on.

*Expressivity* is orthogonal to the question about *constituency vs. dependency*: e.g. [Combinatory Categorial Grammar](https://en.wikipedia.org/wiki/Combinatory_categorial_grammar) and X-bar are both based on constituency, but they are in different level in the Chomsky hierarchy. [Functional Dependency Grammar](https://helda.helsinki.fi/bitstream/handle/10138/19246/parsingi.pdf) is a dependency-based formalism that can express constructs beyond context-free: see Chapter **3.4 Expression power** starting from page 22 in the linked document.

