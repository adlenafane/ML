import os
import sys
import sqlite3
import cPickle, pprint
from msdSubsetSQL import *

def getTrackIdList(path):
	#Recupere toutes les TrackID dans le fichier dump en entree et les renvoie sous forme de liste
	with open(path, 'rb') as f:
		X = cPickle.load(f)
	result=[]
	for element in X:
		result.extend(element[1])
	#print "Longueur est %d" %len(result)
	return result
#------------------------------------------------------------------------------ 
#LastFm database connection
path_to_LFM_DB = ('/Users/nicolas/Documents/2012-2013/APA/Projet')
#Check path
assert os.path.isdir(path_to_LFM_DB),'Wrong path to the database!'
# Accessing the database
conn = sqlite3.connect(os.path.join(path_to_LFM_DB, 'lastfm_similars.db'))
#------------------------------------------------------------------------------ 
def getSimilar(TrackID):
	sql = "SELECT target FROM similars_src WHERE tid='%s'" % TrackID
	res = conn.execute(sql)
	queryRes=res.fetchone()
	if queryRes == None:
		result=[]
	else:
		data = queryRes[0]
		result = []
		for idx, d in enumerate(data.split(',')):
		    if idx % 2 == 0:
		        pair = [d]
		    else:
		        pair.append(float(d))
		        result.append(pair)
		#sort our output
		result = sorted(result, key=lambda x: x[1], reverse=True)
	return result

def generateSimilDic(trackList):
	simDic={}
	dump_path="/Users/nicolas/Documents/2012-2013/APA/Projet/ML2/"
	for trackID in trackList:
		#We get the similar songs
		similarList=getSimilar(trackID)
		#We insert in our simDic the songs taht are also in our MSD subset
		simDic[trackID]=getTracksInSubset(similarList)
		print "Similar songs to " + trackID + "added"

	with open(dump_path + 'similarityDic.txt', 'wb') as f:
		cPickle.dump(simDic, f)
	return simDic	

#------------------------------------------------------------------------------ 
#Generate dump file
#print generateSimilDic(getTrackIdList("/Users/nicolas/Documents/2012-2013/APA/Projet/rawOutputtrackid.txt"))
#------------------------------------------------------------------------------ 
#Generate stats about similarity set
with open("/Users/nicolas/Documents/2012-2013/APA/Projet/ML2/similarityDic.txt", 'rb') as f:
	X = cPickle.load(f)
print computeSimilarityStats(preprocessForSimilarity(X))

#------------------------------------------------------------------------------ 
#TESTS
"""
print "Tests"
#print getTrackIdList("/Users/nicolas/Documents/2012-2013/APA/Projet/rawOutputtrackid.txt")
simlst=getSimilar("TRAAAAW128F429D538")
print simlst
print getTracksInSubset(simlst)
print getTracksInSubset([])
"""

