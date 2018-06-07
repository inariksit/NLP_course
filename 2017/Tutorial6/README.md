## Q1: IOB

Using only IO, without B, would create ambiguities in cases like "Mary showed John Gothenburg" -- if both John and Gothenburg are tagged as I, it's ambiguous whether they are one entity or two.

Next question, is chunking parsing? And how about chinking (i.e. specify holes outside chunks, so you get left
with chunks)? 

An important distinction between chunking and full parsing is that chunks can't be recursive. As many of you noted, chunking is called often shallow or partial parsing. 
So yes, for some values of parsing! I wasn't really interested in a right or wrong answer, just the reasons. :-)

As for chunking and chinking, I'll just quote your answers:

> I would say that chunking creates more structure, as it tags the chunks it creates. As chinking doesn’t label the structures it creates when dividing the chunks, it doesn’t really give any meaning to the structures

> With chinking, we target the token sequences that we don’t want to include in our chunks. For this reason, I believe that chinking 
creates less structure than chunking. With chunking, we select and label specific chunk types. But with chinking we just find the stuff we want to exclude and 
keep everything else. The removal of the non-target tokens doesn’t tell us anything about the remaining chunks aside from being within the target chunk categories.

> [Chinking] works in a different way as chunking, but the final structure should also be considered a simple way of parsing.  The amount of structure that chinking creates, as compared to chunking, would depend on the way each of these taggers are built, I don’t think you can tell generically which one creates more or less structure.

## Q2: Information extraction in the wild

Note: I don't know what techniques are actually used in the website, the point was just to practice the concepts that you learned at the lecture. Here's a list of things you mentioned--it's irrelevant if some of them are actually not used.

* Scraping / cleaning (removing formatting)
* Sentence segmentation
* Tokenisation
* Stemming
* Regular expressions
* POS tagging
* Syntactic parsing / dependency parsing
* Named entity recognition 
* Keyword extraction
* Relation detection
* Reference resolution
* Event detection
* Temporal expression recognition
* Classification
* Sentiment analysis
* Summarisation

