"""
    Script to import and transform data from the MillionSongSubset

    Inspired by the work of :
    Thierry Bertin-Mahieux (2010) Columbia University
    tb2332@columbia.edu
"""
# usual imports
import os
import time
import glob
import datetime
import cPickle
import numpy as np

# path to the Million Song Dataset subset (uncompressed)
msd_subset_path='../MillionSongSubset'
msd_subset_data_path=os.path.join(msd_subset_path,'data')
msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
assert os.path.isdir(msd_subset_path),'wrong path' # sanity check

all_desired_data = []
all_desired_data_normalized = []
elementsRequested = []

# imports specific to the MSD
import hdf5_getters as GETTERS

# the following function simply gives us a nice string for
# a time lag in seconds
def strtimedelta(starttime,stoptime):
    return str(datetime.timedelta(seconds=stoptime-starttime))

# we define this very useful function to iterate the files
def apply_to_all_files(basedir, func=lambda x, y: x,ext='.h5'):
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



match_songId_row = {}

# we define the function to apply to al_l files
def func_to_get_desired_values(filename, count):
    """
    This function does 3 simple things:
    - open the song file
    - get the elements we want and put them in
    - close the file
    INPUT : 
    filename    - The name of the h5 file to be loaded
    count       - The value of the current row to be loaded
    """
    global all_desired_data
    # Open file
    h5 = GETTERS.open_h5_file_read(filename)
    
    # Add to the dictionnary the correspondance between row and song_id
    match_songId_row[count] = GETTERS.get_song_id(h5)

    # Create and fill a record
    record = []
    for element in elementsRequested:
        record.append(getattr(GETTERS, element)(h5))
    
    # Add the record to the data
    all_desired_data[count] = record
    h5.close()

def createNormalizedVector():
    '''
    From a vector containing all data, create the "normalized" version e.g. value
    minus the minimum divided by the range 
    --> Vector with same shape but values between 0 and 1
    '''
    global all_desired_data_normalized
    all_desired_data_normalized = all_desired_data

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

    record_index = 0
    for record in all_desired_data:
        for i in range(len(min_array)):
            if range_array[i] != 0:
                all_desired_data_normalized[record_index][i] = (record[i] - min_array[i]) / range_array[i]
            else:
                pass
        record_index+=1
    return all_desired_data_normalized

def createDataDump(filename):
    '''
        From 2 vectors (one raw and one normalized) create the cPickle dumps
    '''
    # Save raw output
    with open('rawOutput' + filename + '.txt', 'wb') as f:
        cPickle.dump(all_desired_data, f)

    with open('rawOutputExtract' + filename + '.txt', 'wb') as f:
        extract = []
        for i in range(100):
            extract.append(all_desired_data[i])
        cPickle.dump(extract, f)

    # with open('normOutput' + filename + '.txt', 'wb') as f:
    #     cPickle.dump(all_desired_data_normalized, f)

    # with open('normOutputExtract' + filename + '.txt', 'wb') as f:
    #     extract = []
    #     for i in range(100):
    #         extract.append(all_desired_data_normalized[i])
    #     cPickle.dump(extract, f)

    # with open('normOutputClean' + filename + '.txt', 'wb') as f:
    #     extract = []
    #     for i in range(len(all_desired_data_normalized)):
    #         dataOk = True
    #         for j in all_desired_data_normalized[i]:
    #             # We assume that 0 means not analyzed so we do not keep it
    #             if j==0:
    #                 dataOk = False
    #                 break
    #         if dataOk:
    #             extract.append(all_desired_data_normalized[i])
    #     cPickle.dump(extract, f)

def createDesiredVector(elementsRequestedInput, filename):
    '''
        Will probably be used with a Flask server to retrieve the desired parameters
        1. Create the shape of the output
        2. Go through all files and retrieve the desired values
        3. Create a normalized version of the output
        4. Dump the 2 vectors
    '''
    print '##### Beginning Extration #####'
    global elementsRequested
    global all_desired_data
    global all_desired_data_normalized

    elementsRequested = elementsRequestedInput
    print "elementsRequested", elementsRequested

    # Get the number of files
    numberOfSongs = apply_to_all_files(msd_subset_data_path)
    print 'Number of song files:', numberOfSongs

    # The parameters of the createDesired function and the shape size must me dynamics
    global all_desired_data 
    all_desired_data = np.empty(shape=(numberOfSongs,len(elementsRequested)))
    print 'Output vector base prefilled'

    # Go through all files and apply the function to get data
    t1 = time.time()
    apply_to_all_files(msd_subset_data_path, func=func_to_get_desired_values)
    t2 = time.time()
    print 'all data extracted in:',strtimedelta(t1,t2)

    # Create a normalized vector of the data
    #all_desired_data_normalized = createNormalizedVector()
    #print "Data normalized"

    # Dump data with cPickle
    createDataDump(filename)
    print "Data dumped!!"
    print '##### End of Extration #####'