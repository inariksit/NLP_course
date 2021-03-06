## Q1: Humour explained

Why are the following sentences (supposed to be) funny? Explain with your newfound knowledge of lexical semantics.

* The fancy name for the phenomenon: https://en.wikipedia.org/wiki/Zeugma_and_syllepsis

* The word *inlict* is more commonly used for acts of violence or disease, and thus using it in the context of naming a child is meant to be humorous, and also reveal what the speaker thinks of the name.

* Homonymy, but not homophony; only works in written.

Some picks of your examples:

> “Why do francophones eat only one egg for breakfast?”  “Because one egg is *un oeuf*”

> (Conversation between A and B, on the topic of A wanting to own horses in the future. B's reply:)
“It will at least have to wait until you are in a more stable situation.”

> “Come to the nerd side, we have pi”

> “Why was a linguist banned from a linguistics conference?” “They failed the [wug test](https://en.wikipedia.org/wiki/Jean_Berko_Gleason#Children.27s_learning_of_English_morphology.E2.80.8D.E2.80.94.E2.80.8Cthe_Wug_Test)” 

## Q2: NLTK document classifier

See comments from last year: https://github.com/inariksit/NLP_course/tree/master/2016/Tutorial4#q1-lessons-on-statistical-relevance

## Q3: Everything explained

Related to language identification, here's an exercise in reverse engineering: type short combinations of letters into [Google Translate](https://translate.google.com/) and ask it to identify the language ^_^

## Q4: Entropy

Comments from last year: https://github.com/inariksit/NLP_course/tree/master/2016/Tutorial4#q3-entropy-and-classeslabelscategories

General note on Python lists and tuples: many of you do like this:

```python
names = ["Bella", "Max", "Max"]
species = ["human", "dog", "human"]
names_species_strings = ["Bella human", "Max dog", "Max human"] 
# or a version with tuples
names_species_tuples = [("Bella","human"), ("Max","dog"), ("Max","human")] 
```

To save some typing, you could use the `zip` function, which takes two or more lists, and produces a list of tuples. For example, `zip([1,2],['a','b'])` produces the list `[(1,'a'),(2,'b')]`.

```python
names = ["Bella", "Max", "Max"]
species = ["human", "dog", "human"]
names_species_zipped = zip(names,species)
```

Or if you specifically want to have strings, you could do the following with list comprehensions:

```python
[n + s for (n, s) in names_species_zipped]
```
