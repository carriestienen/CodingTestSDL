
def lists_overlap(a, b):
    for i in a:
        if i in b:
            return True
    return False

def generate_ngrams(s, n):

    words = [word for word in s.split(" ") if word != ""]

    ngrams = zip(*[words[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

def removeoverlap(test,train):
    #small is test; large is train

    testfile = open(test,'r')
    test_sentences = testfile.readlines()

    trainfile = open(train,'r')
    train_sentences = trainfile.readlines()

    for test_line in test_sentences:
        if test_line in train_sentences:
            train_sentences.remove(test_line)
        else:
            for train_line in train_sentences:
                test_ngrams = generate_ngrams(test_line,7)
                train_ngrams = generate_ngrams(train_line,7)

                if lists_overlap(test_ngrams,train_ngrams):
                    train_sentences.remove(train_line)

    outputfile = open("output.txt","w")
    outputfile.writelines(train_sentences)

#removeoverlap("test.txt","train.txt")