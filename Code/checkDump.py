import cPickle, pprint

with open('./dump/normOutputCleanadlen.txt', 'rb') as f:
    X = cPickle.load(f)

pprint.pprint(X)
print 'lenght', len(X)

for x in X:
	for tag in x[0][3]:
		print tag