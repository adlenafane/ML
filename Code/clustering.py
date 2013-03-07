import numpy as np
import cPickle,pprint

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

def getClusteringScore(clusterList,similDic):
	score=0
	for cluster in clusterList:
		for trackId in cluster:
			similarSongs=similDic[trackId]
			for similTrack in similarSongs:
				if similTrack!=None:
					if similTrack[0] in cluster:
						score = score + similTrack[1]*1

	return score
#------------------------------------------------------------------------------ 
#TESTS
"""
with open("/Users/nicolas/Documents/2012-2013/APA/Projet/ML2/similarityDic.txt", 'rb') as f:
	X = cPickle.load(f)
print getClusteringScore([['TRAAMPA128F92E7D0D','TRAYYAU128F92D58D0','TRBEBNV128F423783D']],X)
"""
