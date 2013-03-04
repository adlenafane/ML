import pprint, cPickle

with open('rawOutputTest.txt', 'rb') as f:
    X = cPickle.load(f)

pprint.pprint(X)