# Q1: lessons on statistical relevance

This was another of these assignments where you may well find flaws in the method. Note that I don't know how is NLTK's "most informative words" feature implemented, but based on your results, it is biased towards rare words.

An example: we have 500,000 blue stones and 500,000 red stones. If we put all of them in one massive jar, randomly shuffled, on the average we should be drawing around 50 % blue and 50 % red stones. But if we distribute these stones into smaller jars that only fit 100, it's likely that some of these 100-stone jars are highly skewed: mostly blue or mostly red.

Likewise, if some word only appears in 100 reviews, it's a higher chance that these 100 movies happen to be majority positive or negative, and the word is not doing much as an indicator. There are many rare words, it is likely that *some* of them produce this statistical artifact.

# Q2: more resources

### Learn about Bayes' rule
* https://arbital.com/p/bayes_rule/?l=1zq

### Poetry generated by distributional semantics
* http://www.peerpress.co.uk/discoursecpp.pdf

### Gendered language and word embeddings:
* http://bookworm.benschmidt.org/posts/2015-10-30-rejecting-the-gender-binary.html
* http://www.npr.org/sections/alltechconsidered/2016/08/12/489507182/hes-brilliant-shes-lovely-teaching-computers-to-be-less-sexist

### Further material on classification / machine learning / ...

> I think the easiest option is to install some library and follow tutorials related to that library. In the MLT machine learning course, we use a library called scikit-learn, which I think is quite easy to use:
> 
> http://scikit-learn.org/stable/
> 
> There are quite a few tutorials and examples on their webpage, for instance
> 
> http://scikit-learn.org/stable/tutorial/index.html
> 
> There are also more advanced toolkits for the people who want to develop their own architectures. (Scikit-learn is more of a collection of "black boxes".) Google's TensorFlow is probably the one that is most popular now. It also comes with extensive tutorials.
> 
> https://www.tensorflow.org/versions/r0.12/tutorials/index.html
> 
> The webpage of the MLT machine learning course also has a few pointers to literature:
> 
> https://svn.spraakdata.gu.se/repos/richard/pub/ml2016_web/index.html


# Q3: Entropy and classes/labels/categories

A collection has a maximal entropy if all the values in it are evenly distributed. If there are only two classes, then the maximum value for the entropy is 1, and that is reached when there are same number of words in each class. But if there are more classes, then the number can be higher. If you can draw any item of, say, 10 classes, you will be more surpised at whatevery you get, than if you could only get items of 2 classes.


* 100 aardvarks: you expect aardvarks and you always get aardvarks. Entropy 0, you're never surprised.
* 99 aardvarks - 1 horse: you expect mostly aardvarks and you mostly get aardvarks. Entropy is very small, you're very rarely surprised.
* 50 aardvarks - 50 horses: you can't rely on any great strategy to guess which animal you get, but it's still pretty safe: it can only be an aardvark or a horse. Entropy 1, you're sort of mildly surprised all the time. Note it has nothing to do with the absolute value. The entropy is the same for 3 horses - 3 aardvarks as it is for 300 horses and 300 aardvarks.
* 2 aardvarks - 2 horses - 2 kangaroos - 2 dinosaurs ... - 2 warthogs: you live in the state of great uncertainty, any kind of animal out of 50 may appear at your door. Entropy is high, you're really surprised all the time.

