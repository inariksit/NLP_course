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

#### 1. count(x) ≈ count(y) ≈ count(x,y)

In the first scenario, x and y appear almost always together, ie. hardly ever alone.
We can subdivide this into the following cases:

##### 1a) Frequent x and y: *count(x) ≈ count(y) ≈ count(x,y) ≈ corpus_size*

The words `x` and `y` appear in almost every document. Let us assume there are only `p` documents where they don't appear. (If they appear in literally every document, what happens then?)
Think for instance `PMI(and, this)`:

```
     (corpus_size-p) * corpus_size               corpus_size
log ___________________________________ = log _________________ = log 1.000...tiny  ≈ 0.0000...tiny
     (corpus_size-p) * (corpus_size-p)         corpus_size - p
     
```

PMI is tiny for two frequent words, even though they are hardly ever without one another.

With LMI, we multiply the tiny PMI with the huge `count(x,y)`, and get something less tiny.

In practice, LMI is still tiny but not really massively tiny like PMI.

##### 1b) Rare x and y: *count(x) ≈ count(y) ≈ count(x,y) ≈ 1*

The words `x` and `y` are rare on their own and hence rare together. 
For example, *sAiMZzqGdkpuJyWwIYMvZahVqVo* (I just decided that means *hello* in my brand new conlang!) has one hit–this page–and *ἐκβουτῠπόομαι* has 192 hits.
(192 is totally ≈1 when we compare to the count for *this* or *and* or *school*. :-P)
This document is the only one that uses them together.
We calculate `PMI(sAiMZzqGdkpuJyWwIYMvZahVqVo, ἐκβουτῠπόομαι)`:

```
    1 * corpus_size
log ________________ = log corpus_size/192 = quite big number
      1 * 192
```

With LMI, we multiply the quite big PMI with the small `count(x,y)` and the final LMI score will stay big.

Compared to the previous, the difference in LMIs is smaller than the difference in PMIs:

* PMI(and, this) = tiny
* PMI(sAiMZzqGdkpuJyWwIYMvZahVqVo, ἐκβουτῠπόομαι) = big

* LMI(and,this) = tiny * (corpus_size-p)
* LMI(sAiMZzqGdkpuJyWwIYMvZahVqVo, ἐκβουτῠπόομαι) = big * 1


#### 2. *count(x) ≈ corpus_size* and *count(y) ≈ count(x,y) ≈ 1*
 
One of the words is really common and the other is really infrequent. For instance, `PMI(those, ἐκβουτῠπόομαι)`:

```
       ~1 * corpus_size             corpus_size
log _____________________  ≈ log _________________ = tiny number
     (corpus_size-p) * ~1         corpus_size - p
```

PMI gives the same tiny number as the scenario `1a)`. But LMI shows the difference: here `count(x,y)` is tiny, and when we multiply PMI by it, the LMI is also tiny.

So, PMI gives equal results to the following scenarions, but LMI gives the first one better result and the second one worse.
* `frequent x, frequent y, frequent x&y` (and, this)
* `frequent x, rare y, rare x&y` (those, ἐκβουτῠπόομαι)

**How does this scale to the more common scenarios, with aardvarks, logarithms, googleology and science?**

#### 3. *count(x) ≈ count(y) ≈ corpus_size* and *count(x,y) ≈ 1*

http://www.googlewhack.com/ was created to answer this question. 