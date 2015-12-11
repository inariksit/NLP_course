# LT2113 H15 Natural language processing: Tutorial 3

## Q1. More about entropy

## Q2. Parsing: a summary

Some terms resulted in more confusion than others. I address common issues below, and individual feedback for more specific things.

### Generative grammar

There is a lot of association with Chomsky, or whether generative grammar is something that models how human brain works. (TODO)

### Dependency grammar

Dependency grammar is also a form of generative grammar. 
It is contrasted with a **phrase structure grammar** or **constituency grammar** (those two are basically the same thing).


### Reductionist grammar

Now onto something that is not a generative!
A **reductionist** grammar formalism is constrasted with a **licencing** (or, *generative*!) grammar formalism. An empty reductionist grammar allows all possible strings in the world, whereas an empty licencing grammar allows no string.
[Constraint Grammar](http://beta.visl.sdu.dk/constraint_grammar.html) (CG) is an example of a reductionist system. The starting point is that the words can have any analysis provided by a morphological analyser, and the task of the constraint rules is to get rid of inappropriate analyses. A perfect CG leaves only the right POS tags (=more structure than we started with!), and an empty CG leaves in place all the POS tags.


### Expressivity

A couple of terms were related to the expressivity of the grammars: **regular grammar** and **context-free grammar**.
Many of you mentioned the [Chomsky hierarchy](https://en.wikipedia.org/wiki/Chomsky_hierarchy#Summary). Regular grammars are the least expressive, and context-free grammars come after regular grammars. You might find the numbering confusing or intuitive (Type-0=most expressive, Type-3=least expressive)--don't worry about remembering a number, try to get an intuition about what kinds of production rules the grammars allow, what kinds of strings they accept and so on.

*Expressivity* is orthogonal to the question about *constituency vs. dependency*: e.g. [Combinatory Categorial Grammar](https://en.wikipedia.org/wiki/Combinatory_categorial_grammar) and X-bar are both based on constituency, but they are in different level in the Chomsky hierarchy. (Don't worry if you don't know what CCG is!)


## Q3-Q5. IOB and evaluation metrics

## Q6. Meta

## Bonus questions

