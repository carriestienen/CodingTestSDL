import numpy as np

def generate_ngrams(s, n):

    words = [word for word in s.split(" ") if word != ""]

    ngrams = zip(*[words[i:] for i in range(n)])
    ngrams = [" ".join(ngram) for ngram in ngrams]

    for ngram in np.unique(ngrams):
        print(ngram + " = " + str(ngrams.count(ngram)))

'''s = "it's not the size of the dog in the fight , it's the size of the fight in the dog ."
print(generate_ngrams(s,1))
print(generate_ngrams(s,2))'''