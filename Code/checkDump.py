import cPickle, pprint

def checkDump(filename = './dump/normOutputCleanadlen.txt'):
	with open(filename, 'rb') as f:
	    X = cPickle.load(f)

	pprint.pprint(X)
	print 'lenght', len(X)

	for x in X:
		for tag in x[0][3]:
			print tag
	return X

checkDump('./dump/rawOutputtrackid.txt')