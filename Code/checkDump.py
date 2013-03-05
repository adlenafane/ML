import cPickle, pprint

with open('normOutputCleanfullNorm.txt', 'rb') as f:
    X = cPickle.load(f)

pprint.pprint(X)
print 'lenght', len(X[0])