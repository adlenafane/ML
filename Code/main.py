import os, sys, time, glob, datetime, pprint
import h5py
import hdf5_getters
import sqlite3
import numpy as np

#import hdf5_getters as GETTERS

msd_subset_path='C:\Users\Adlen\Documents\GitHub\ML\MillionSongSubset'
msd_subset_data_path=os.path.join(msd_subset_path,'data')
msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
assert os.path.isdir(msd_subset_path),'wrong path' # sanity check

#sys.path.append( os.path.join(msd_code_path,'PythonSrc') )

#------------------------------------------------------------------------------ 
def strTimeDelta(starttime, stoptime):
	return str(datetime.timedelta(seconds=stoptime - starttime))
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# Function to iterate throught files
def applyToAllFiles(basedir, func = lambda x: x, ext= '.h5'):
	"""
	From a base directory, go through all subdirectories,
	find all files with the given extension, apply the
	given function 'func' to all of them.
	If no 'func' is passed, we do nothing except counting.
	INPUT
		basedir  - base directory of the dataset
		func     - function to apply to all filenames
		ext      - extension, .h5 by default
		RETURN
		number of files
	"""
	cnt = 0
	# iterate over all files in all subdirectories
	for root, dirs, files in os.walk(basedir):
		files = glob.glob(os.path.join(root,'*'+ext))
		# count files
		cnt += len(files)
		# apply function to all files
		for f in files :
			func(f)
	return cnt
#------------------------------------------------------------------------------ 


#------------------------------------------------------------------------------ 
def getArtistName(filename):
	"""
	This function does 3 simple things:
	- open the song file
	- get artist ID and put it
	- close the file
	"""
	with h5py.File(filename) as h5:
		artist_name = h5py.get_artist_name(h5)
		all_artist_names.add( artist_name )
#------------------------------------------------------------------------------ 


#print 'number of song files:', applyToAllFiles(msd_subset_data_path)

allArtistNames = set()

h5 = h5py.File('C:\Users\Adlen\Documents\GitHub\ML\MillionSongSubset\data\A\A\A\TRAAAAW128F429D538.h5')
list_of_names = []
h5.visit(list_of_names.append)
pprint.pprint(list_of_names)

print '\n'

h5 = h5py.File('C:\Users\Adlen\Documents\GitHub\ML\MillionSongSubset\AdditionalFiles\subset_msd_summary_file.h5')
list_of_names = []
h5.visit(list_of_names.append)
pprint.pprint(list_of_names)

'''
t1 = time.time()
applyToAllFiles(msd_subset_data_path,func=getArtistName)
t2 = time.time()
print 'all artist names extracted in:',strtimedelta(t1,t2)
'''