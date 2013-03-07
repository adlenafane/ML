import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import cPickle
#import pprint
from clustering import *

def numberOfInfos(rawData):
	#Recupere le nombre de categories d infos disponibles pour decrire le dataset
	return len(rawData[0][0])

def prepareData(rawData):
	result=[]
	for elementList in rawData:
		result.append(elementList[1])
	return np.asarray(result)

def applyMeanShift(data,quantileValue=0.2,clusterall=True):
	result=[]
	n_samples=len(data)
	print "Nombre de points du dataset: %d" %n_samples
	
	bandwidth = estimate_bandwidth(data, quantile=quantileValue)
	ms = MeanShift(bandwidth=bandwidth,cluster_all=clusterall)
	#Applique le MeanShift
	clustereddata=ms.fit(data)
	clusteredlabels= clustereddata.labels_
	barycenters=ms.cluster_centers_

	labels_unique = np.unique(clusteredlabels)
	nbOfClusters = len(labels_unique)

	print "number of estimated clusters : %d" % nbOfClusters

	for i in labels_unique:
		print "###Indices des points du cluster %d : ###" %i
		# print [indice[0] for indice in np.argwhere(clusteredlabels == i)]
		result.append([indice[0] for indice in np.argwhere(clusteredlabels == i)])
	#Add a zero coordinates vector to takeinto account the fact that -1 "cluster" does not have a barycenter
	if -1 in labels_unique:
		barycenters= np.append([[0 for k in range(len(barycenters[0]))]],barycenters,axis=0)

	return [result,barycenters]

def meanShiftTreatment(dataPath):
	with open(dataPath, 'rb') as f:
		data = cPickle.load(f)
	nbOfInfos = numberOfInfos(data)
	clusterList = []
	barycentersList = []
	infosList =[]
	#Get the data in the suitable format for applying MeanShift
	processedData=prepareData(data)
	#Run the MeanShift on the data
	meanShiftOutput= applyMeanShift(processedData)
	#By cluster - give the songId for each song
	clusterList=songIdsClustersList(meanShiftOutput[0],data)
	#Update barycenters list
	barycentersList=meanShiftOutput[1]
	#Update infoList list
	if nbOfInfos != 1:
		for infoNb in range(1,nbOfInfos):
			infosList.append(getInfo(meanShiftOutput[0],data,infoNb))

	pprint.pprint(barycentersList)
	return clusterList, barycentersList, infosList

#TESTS
"""
print "TESTS"


#with open('/Users/nicolas/Documents/2012-2013/APA/Tests Algos/normOutputCleanNicoKmeans4.txt', 'rb') as f:
with open('/Users/nicolas/Documents/2012-2013/APA/Tests Algos/normOutputCleanTest.txt', 'rb') as f:
    data = cPickle.load(f)
print "###Data ###"
#pprint.pprint(data)
print "Number of Infos: "
print numberOfInfos(data)
print "prepareData:"
dataToCluster= prepareData(data)
#pprint.pprint(dataToCluster)
print applyMeanShift(dataToCluster)
"""
"""
print 50*"_"
print "meanShiftTreatment: "
print meanShiftTreatment('/Users/nicolas/Documents/2012-2013/APA/Tests Algos/normOutputCleanTest.txt')
print meanShiftTreatment('/Users/nicolas/Documents/2012-2013/APA/Tests Algos/normOutputCleanNicoKmeans4.txt')
"""