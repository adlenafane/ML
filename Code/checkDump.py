import cPickle, pprint

with open('./dump/normOutputCleanNicoTestKMeans2.txt', 'rb') as f:
    X = cPickle.load(f)

pprint.pprint(X)
print 'lenght', len(X)