import nltk
import math

def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p * math.log(p,2) for p in probs)


a = ["spam", "spam", "spam"]
b = ["spam", "spam", "ham", "ham"]
c = ["horse", "giraffe", "horse", "aardvark", "kangaroo", "aardvark"]

names   = ["Max","Rex","Brutus","Lulu","Max","Bella","Max","Lulu"]
species = ["dog","dog","dog","dog","human","human","dog","human"]
n_s = list(zip(names, species))

for l in [a,b,c,n_s,names,species]:
  print(entropy(l))


#Another way for handling lists of pairs:
d_i    = [("max","dog"), ("rex","dog"), ("brutus","dog"),("lulu","dog"), ("max","human"), ("bella","human"), ("max","dog"), ("lulu","human")]
d_ii   = [a for (a,b) in d_i]
d_iii  = [b for (a,b) in d_i]
