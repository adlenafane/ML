# usual imports
import os
import sys
import time
import glob
import datetime
import cPickle
import numpy as np # get it at: http://numpy.scipy.org/
# path to the Million Song Dataset subset (uncompressed)
# CHANGE IT TO YOUR LOCAL CONFIGURATION
msd_subset_path='../MillionSongSubset'
msd_subset_data_path=os.path.join(msd_subset_path,'data')
msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
assert os.path.isdir(msd_subset_path),'wrong path' # sanity check

# imports specific to the MSD
import hdf5_getters as GETTERS

# the following function simply gives us a nice string for
# a time lag in seconds
def strtimedelta(starttime,stoptime):
    return str(datetime.timedelta(seconds=stoptime-starttime))

# we define this very useful function to iterate the files
def apply_to_all_files(basedir,func=lambda x, y: x,ext='.h5'):
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
    count = 0
    # iterate over all files in all subdirectories
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        # count files
        cnt += len(files)
        # apply function to all files
        for f in files :
            print "count", count
            func(f, count)
            count+=1
    return cnt

# Get the number of files
numberOfSongs = apply_to_all_files(msd_subset_data_path)
print 'number of song files:', numberOfSongs

# let's now get all artist names in a set(). One nice property:
# if we enter many times the same artist, only one will be kept.
all_desired_data = np.empty(shape=(numberOfSongs,6))
match_songId_row = {}

# we define the function to apply to al_l files
def func_to_get_desired_values(filename, count):
    """
    This function does 4 simple things:
    - open the song file
    - get the elements we want and put them in
    - close the file
    """
    # Open file
    h5 = GETTERS.open_h5_file_read(filename)
    
    # Add to the dictionnary the correspondance between row and song_id
    match_songId_row[count] = GETTERS.get_song_id(h5)

    # Create and fill a record
    record = []
    
    #record.append(GETTERS.get_danceability(h5))
    record.append(GETTERS.get_duration(h5))
    #record.append(GETTERS.get_energy(h5))
    record.append(GETTERS.get_loudness(h5))
    record.append(GETTERS.get_mode(h5))
    record.append(GETTERS.get_tempo(h5))
    record.append(GETTERS.get_time_signature(h5))
    record.append(GETTERS.get_year(h5))
    
    record = np.array(record)
    
    # Add the record to the data
    all_desired_data[count] = record
    h5.close()


# let's apply the previous function to all files
# we'll also measure how long it takes
t1 = time.time()
apply_to_all_files(msd_subset_data_path,func=func_to_get_desired_values)
t2 = time.time()
print 'all artist names extracted in:',strtimedelta(t1,t2)

# Save raw output
with open('rawOutput.txt', 'wb') as f:
    cPickle.dump(all_desired_data, f)

with open('rawOutputExtract.txt', 'wb') as f:
    extract = []
    for i in range(100):
        extract.append(all_desired_data[i])
    cPickle.dump(extract, f)

# Save match
with open('correspondance.txt', 'wb') as f:
    cPickle.dump(match_songId_row, f)

# let's see some of the content of 'all_desired_data'
print 'found',len(all_desired_data),'songs records'
for k in range(5):
    print all_desired_data[k]

# Let's normalize these data to have more similar values
min_array = [0]*len(all_desired_data[0])
max_array = [0]*len(all_desired_data[0])
range_array = [0]*len(all_desired_data[0])

for i in range(len(all_desired_data[0])):
    min_array[i] = all_desired_data[0][i]
    max_array[i] = all_desired_data[0][i]

for record in all_desired_data:
    for i in range(len(min_array)):
        if record[i] < min_array[i]:
            min_array[i] = record[i]
        elif max_array[i] < record[i]:
            max_array[i] = record[i]

for i in range(len(min_array)):
    range_array[i] = max_array[i] - min_array[i]

for record in all_desired_data:
    for i in range(len(min_array)):
        if range_array[i] != 0:
            record[i] = (record[i] - min_array[i]) / range_array[i]
        else:
            pass

# Let's take a look inside
for k in range(5):
    print all_desired_data[k]

# Save normalized output
with open('normOutput.txt', 'wb') as f:
    cPickle.dump(all_desired_data, f)

with open('normOutputExtract.txt', 'wb') as f:
    extract = []
    for i in range(100):
        extract.append(all_desired_data[i])
    cPickle.dump(extract, f)

with open('normOutputClean.txt', 'wb') as f:
    extract = []
    for i in range(len(all_desired_data)):
        if all_desired_data[i][0] != 0 and all_desired_data[i][1] != 0 and all_desired_data[i][2] != 0 and all_desired_data[i][3] != 0 and all_desired_data[i][4] != 0 and all_desired_data[i][5] != 0 :
            extract.append(all_desired_data[i])
    cPickle.dump(extract, f)