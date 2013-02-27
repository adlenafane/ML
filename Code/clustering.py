import os
import sqlite3
import time
import datetime
import numpy
import matplotlib.pyplot as pyplot

#==============================================================================
# TO CONFIGURE
#==============================================================================

# path to the folder 'AdditionalFiles'
# path_to_DB = ('/home/octave/workspace/Py_ML_Adlen/MillionSongSubset/\
# AdditionalFiles')
path_to_DB = ('../MillionSongSubset/AdditionalFiles')

#==============================================================================

# Checking path & defining a useful function
print(
'Starting "simple_stats.py"...\n\
Looking into folder ' + path_to_DB)
t_start = time.time()
assert os.path.isdir(path_to_DB),'Wrong path to the database!'

#------------------------------------------------------------------------------ 

# gives a nice string for a time lag in seconds (in the form of: hh:mm:ss.xx)
def strtimedelta(start_time,stop_time):
    return str(datetime.timedelta(seconds = stop_time - start_time))

#------------------------------------------------------------------------------ 

#==============================================================================

# Accessing the database and doing some simple stats
print('\nStarting to query the database...')
conn = sqlite3.connect(os.path.join(path_to_DB, 'subset_track_metadata.db'))

#----------------------------------------------------------------------------- 

print('\n* Listing all "artist_name"...')
# building SQL query
q = 'SELECT DISTINCT artist_name FROM songs'

t1 = time.time()
res = conn.execute(q)
all_artist_names = res.fetchall()
t2 = time.time()

print('\t%s artist names found' %len(all_artist_names))
print('Done, all artist names extracted (SQLite) in:' + strtimedelta(t1,t2))

#----------------------------------------------------------------------------- 