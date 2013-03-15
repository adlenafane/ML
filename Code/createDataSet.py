from kMean import kmeanTreatment
#from meanShift import meanShiftTreatment
import cPickle


def Cnp(n,p, l=None, res=None):
    """ Created: 2005.11.05 - Updated:
        Calcul du Cnp - ne pas renseigne l et res lors de l'appel """
    if l is None: l=[]
    if res is None: res=[]
    if p==0:
        res.append(l)
        return 
    if n==0: return  
    l1=list(l)
    l1.append(n)
    Cnp(n-1, p-1, l1, res)
    Cnp(n-1, p, l, res)
    return res

dataset = [\
	'get_artist_hotttnesss', \
	'get_duration', \
	'get_end_of_fade_in', \
	'get_loudness', \
	'get_start_of_fade_out', \
	'get_tempo', \
	'get_segments_confidence', \
	'get_segments_loudness_max', \
	'get_sections_confidence', \
	'get_beats_confidence', \
	'get_bars_confidence', \
	'get_tatums_confidence' \
]

requests = []

# Create the combine we want
# for p in range(11, len(dataset)):
# 	requests = Cnp(len(dataset), p)
# 	print len(requests)

requests = Cnp(len(dataset), 10)

data = []

# Load the 12*6441 vectors
with open('./dump/normOutputCleanevaluation.txt', 'rb') as f:
	data = cPickle.load(f)

i = 0

# For each new dataset we want
for request in requests:
	print "request", i, "out of", len(requests)
	name = ''
	elementsRequestedInput = []
	feature_number = []

	# Generate the name
	for feature in request:
		name+= '_' + str(feature)
		feature_number.append(feature)

	# Pick the data we want
	new_data = []
	for row in data:
		new_info = row[0]
		new_vector = []
		for i in feature_number:
			new_vector.append(row[1][i-1])
		new_data.append([new_info, new_vector])

	print "New data generated"
	
	filename = 'dataset_' + str(len(request)) + '_' + name

	data_path = './dump/normOutputClean' + filename + '.txt'
	# Dump the generated data
	with open(data_path, 'wb') as f:
		cPickle.dump(new_data, f)

	print "Data dumped"

	clusterList, barycentersList, infosList = kmeanTreatment(data_path, 5)

	with open('./cluster/kmean5' + name + '.txt', 'wb') as f:
		cPickle.dump([clusterList, barycentersList, infosList], f)

	print "Kmean 5 ok and dumped"

	clusterList, barycentersList, infosList = kmeanTreatment(data_path, 10)

	with open('./cluster/kmean10' + name + '.txt', 'wb') as f:
		cPickle.dump([clusterList, barycentersList, infosList], f)

	print "Kmean 10 ok and dumped"

	clusterList, barycentersList, infosList = kmeanTreatment(data_path, 20)

	with open('./cluster/kmean20' + name + '.txt', 'wb') as f:
		cPickle.dump([clusterList, barycentersList, infosList], f)

	print "Kmean 20 ok and dumped"

	clusterList, barycentersList, infosList = kmeanTreatment(data_path, 50)

	with open('./cluster/kmean50' + name + '.txt', 'wb') as f:
		cPickle.dump([clusterList, barycentersList, infosList], f)

	print "Kmean 50 ok and dumped"

	clusterList, barycentersList, infosList = kmeanTreatment(data_path, 10)

	with open('./cluster/kmean100' + name + '.txt', 'wb') as f:
		cPickle.dump([clusterList, barycentersList, infosList], f)

	print "Kmean 100 ok and dumped"

	# clusterList, barycentersList, infosList = meanShiftTreatment(data_path)

	# with open('./cluster/meanshift' + name + '.txt', 'wb') as f:
	# 	cPickle.dump([clusterList, barycentersList, infosList], f)
	
	# print "meanshift ok and dumped"
	i+=1
print "End :)"