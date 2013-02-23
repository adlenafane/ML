'''
Extensively based on:

Tutorial for the Million Song Dataset

by Thierry Bertin-Mahieux (2011) Columbia University
   tb2332@columbia.edu
   Copyright 2011 T. Bertin-Mahieux, All Rights Reserved
'''

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
path_to_DB = ('/home/octave/workspace/Py_ML_Adlen/MillionSongSubset/\
AdditionalFiles')
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
print('\n* Listing all "artist_id"...')
# building SQL query
q = 'SELECT DISTINCT artist_id FROM songs'

t1 = time.time()
res = conn.execute(q)
all_artist_IDs = res.fetchall()
t2 = time.time()

print('\t%s artist IDs found' %len(all_artist_IDs))
print('Done, all artist IDs extracted (SQLite) in:' + strtimedelta(t1,t2))
#----------------------------------------------------------------------------- 
print('\n* Counting songs per artist...')
## building SQL query
q = 'SELECT DISTINCT artist_id,Count(track_id) FROM songs'
q += ' GROUP BY artist_id'

t1 = time.time()
res = conn.execute(q)
pop_artists = res.fetchall()
nb_songs = map(lambda x: x[1], pop_artists) # extracting number of songs only

mean = numpy.mean(nb_songs)
std = numpy.std(nb_songs)
max_songs = numpy.max(nb_songs)
min_songs = numpy.min(nb_songs)

# Plotting histogram
bins = numpy.arange(min_songs, max_songs+2, 1) - 0.5
hist = numpy.histogram(nb_songs, bins)[0]

width = 1
center = (bins[:-1]+bins[1:])/2


fig = pyplot.figure()

pyplot.subplot(1,2,1)
pyplot.bar(center, hist, align = 'center', width = width)

pyplot.xlim(min_songs-1, max_songs+1)
pyplot.xticks(center, fontsize = 12)

pyplot.xlabel('Number of songs', fontsize= 12)
pyplot.ylabel('Number of artists')


t2 = time.time()

print('\tmax= %s ; min= %s ; mean= %s ; std= %s' %(max_songs, min_songs,
                                                 round(mean, 2), round(std,2)))
print('Done, extracted (SQLite) and computed in:' + strtimedelta(t1,t2))
#----------------------------------------------------------------------------- 
print('\n* Counting mbtags per artist...')
conn.close()
conn = sqlite3.connect(os.path.join(path_to_DB, 'subset_artist_term.db'))
## building SQL query
q = 'SELECT DISTINCT artist_id, Count(mbtag) FROM artist_mbtag'
q += ' GROUP BY artist_id'

t1 = time.time()
res = conn.execute(q)
tags_artists = res.fetchall()

nb_tags = map(lambda x: x[1], tags_artists) # extracting number of songs only

mean = numpy.mean(nb_tags)
std = numpy.std(nb_tags)
max_tags = numpy.max(nb_tags)
min_tags = numpy.min(nb_tags)

# Plotting histogram
bins = numpy.arange(min_tags, max_tags+2, 1) - 0.5
hist = numpy.histogram(nb_tags, bins)[0]

width = 1
center = (bins[:-1]+bins[1:])/2

pyplot.subplot(1,2,2)
pyplot.bar(center, hist, align = 'center', width = width)

pyplot.xlim(min_tags-1, max_tags+1)
pyplot.xticks(center)

pyplot.xlabel('Number of mbtags')
pyplot.ylabel('Number of artists')

t2 = time.time()

print('\tmax= %s ; min= %s ; mean= %s ; std= %s' %(max_tags, min_tags,
                                                 round(mean, 2), round(std,2)))
print('Done, extracted (SQLite) and computed in:' + strtimedelta(t1,t2))
#----------------------------------------------------------------------------- 

#----------------------------------------------------------------------------- 
# closing the connection to the database
conn.close()
t_end = time.time()
print('\n"simple_stats.py": DONE --executed in: '+ strtimedelta(t_start,t_end))
#
pyplot.savefig('new_fig.pdf', dpi= 100)
pyplot.show()
#
#==============================================================================
# END OF FILE
#