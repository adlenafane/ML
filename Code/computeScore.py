from clustering import getClusteringScoreFromFile
from createVectorCluster import apply_to_all_files

def generateScore(cluster_path):
	score = []
	score.append(apply_to_all_files(cluster_path, func=getClusteringScoreFromFile, ext='.txt'))
	return score

print generateScore('./cluster')