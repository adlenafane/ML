from time import time
import numpy as np
import pylab as pl
import cPickle,pprint

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale

"""
TODO
Clean prints inside functions
"""
def numberOfInfos(rawData):
	#Recupere le nombre de categories d infos disponibles pour decrire le dataset
	return len(rawData[0][0])

def prepareData(rawData):
	result=[]
	for elementList in rawData:
		result.append(elementList[1])
	return result

def applyKmean(data,nbOfClusters,ninit=10):
	result=[]
	n_samples=len(data)
	print "Nombre de points du dataset: %d" %n_samples
	kmeans = KMeans(init='k-means++', n_clusters=nbOfClusters, n_init=ninit)
	#Applique le Kmean
	clustereddata=kmeans.fit(data)
	clusteredlabels= clustereddata.labels_
	barycenters=kmeans.cluster_centers_
	#Type de barycenters est numpy.ndarray

	for i in range(nbOfClusters):
		print "###Indices des points du cluster %d : ###" %i
		print [indice[0] for indice in np.argwhere(clusteredlabels == i)]
		result.append([indice[0] for indice in np.argwhere(clusteredlabels == i)])

	return [result,barycenters]

def getInfo(Kmeanresults,rawData,infoNb):
	result=[]
	for cluster in Kmeanresults:
		clusterInfo={}
		for indice in cluster:
			featureRawData=rawData[indice][0][infoNb]
			#Test pour Mbtags
			if isinstance(featureRawData,np.ndarray):
				for mbtag in featureRawData:
					if mbtag not in clusterInfo:
						clusterInfo[mbtag]=1
					else:
						clusterInfo[mbtag]+=1
			else:
				if featureRawData not in clusterInfo:
					clusterInfo[featureRawData]=1
				else:
					clusterInfo[featureRawData]+=1
		result.append(clusterInfo)
	return result

def songIdsClustersList(clustersResult,rawData):
	result=[]
	for cluster in clustersResult:
		clusterList=[]
		for indice in cluster:
			clusterList.append(rawData[indice][0][0])
		result.append(clusterList)
	return result

def kmeanTreatment(dataPath,nbOfClusters):
	with open(dataPath, 'rb') as f:
		data = cPickle.load(f)
	nbOfInfos = numberOfInfos(data)
	clusterList = []
	barycentersList = []
	infosList =[]
	#Get the data in the suitable format for Kmean
	processedData=prepareData(data)
	#Run the Kmean on the data
	kmeanOutput= applyKmean(processedData,nbOfClusters)
	#By cluster - give the songId for each song
	clusterList=songIdsClustersList(kmeanOutput[0],data)
	#Update barycenters list
	barycentersList=kmeanOutput[1]
	#Update infoList list
	if nbOfInfos != 1:
		for infoNb in range(1,nbOfInfos):
			infosList.append(getInfo(kmeanOutput[0],data,infoNb))

	return clusterList, barycentersList, infosList

def findIntegrityErrorsInData(rawData):
	pbs=[]
	for elementList in rawData:
		for flo in elementList[1]:
			if type(flo)!=float:
				pbs.append([type(flo),flo,elementList[1],elementList[0]])
	return pbs
"""
print "### TESTS: ###"
#data=[[["a"],[0,0]],[["b"],[0,1]],[["c"],[10,0]],[["c"],[10,1]]]

with open('/Users/nicolas/Documents/2012-2013/APA/Tests Algos/normOutputCleanNicoKmeans4.txt', 'rb') as f:
    data = cPickle.load(f)
print "###Data ###"
pprint.pprint(data)
print "Number of Infos: "
print numberOfInfos(data)
print "prepareData:"
dataToCluster= prepareData(data)
print dataToCluster
print 50*"_"
print "Kmean: "
kres= applyKmean(dataToCluster,4)
print "Barycenters:"
print kres[1]
print 50*"_"
print "Cluster Infos Artist Name: "
print getInfo(kres[0],data,1)
print "Cluster Infos Title: "
print getInfo(kres[0],data,2)
print "Cluster Mbtags: "
print getInfo(kres[0],data,3)
"""
print 50*"_"
print "kmeanTreatment: "
#print kmeanTreatment('/Users/nicolas/Documents/2012-2013/APA/Tests Algos/normOutputCleanNicoTestKMeans2.txt',4)
#print kmeanTreatment('/Users/nicolas/Documents/2012-2013/APA/Tests Algos/normOutputCleanNicoTestKMeans5.txt',4)
print kmeanTreatment('/Users/nicolas/Documents/2012-2013/APA/Tests Algos/normOutputCleanTest.txt',4)
