# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app
from createVectorCluster import createDesiredVector
from createVectorCluster import findBestCluster
from kMean import kmeanTreatment
from meanShift import meanShiftTreatment
from pyechonest import config
from pyechonest import song
from collections import OrderedDict
import operator
import requests
import cPickle
config.ECHO_NEST_API_KEY = "JKVBCIDFBTBNKAVH0"

@app.route('/')
@app.route('/index')
def index():
    rows = \
    [\
        {"function": 'get_artist_familiarity', "description": "FLOAT - artist familiarity"},\
        {"function": 'get_artist_hotttnesss', "description": "FLOAT - artist hotttnesss"},\
        #{"function": 'get_artist_id', "description": "STRING - artist id"},\
        #{"function": 'get_artist_mbid', "description": "STRING - artist mbid"},\
        #{"function": 'get_artist_playmeid', "description": "INT - artist playmeid"},\
        #{"function": 'get_artist_7digitalid', "description": "INT - artist 7digitalid"},\
        {"function": 'get_artist_latitude', "description": "FLOAT - artist latitude"},\
        {"function": 'get_artist_longitude', "description": "FLOAT - artist longitude"},\
        {"function": 'get_artist_location', "description": "STRING - artist location"},\
        {"function": 'get_artist_name', "description": "STRING - artist name"},\
        {"function": 'get_release', "description": "STRING - release"},\
        #{"function": 'get_release_7digitalid', "description": "INT - release 7digitalid"},\
        {"function": 'get_song_id', "description": "STRING - song id"},\
        {"function": 'get_song_hotttnesss', "description": "FLOAT - song hotttnesss"},\
        {"function": 'get_title', "description": "STRING - title"},\
        #{"function": 'get_track_7digitalid', "description": "INT - track 7digitalid"},\
        #{"function": 'get_similar_artists', "description": "ARRAY STRING - similar artists"},\
        #{"function": 'get_artist_terms', "description": "ARRAY - STRING - artist terms"},\
        #{"function": 'get_artist_terms_freq', "description": "ARRAY FLOAT - artist terms freq"},\
        #{"function": 'get_artist_terms_weight', "description": "ARRAY FLOAT - artist terms weight"},\
        {"function": 'get_analysis_sample_rate', "description": "FLOAT - analysis sample rate"},\
        {"function": 'get_audio_md5', "description": "STRING - audio md5"},\
        {"function": 'get_danceability', "description": "****** FLOAT - danceability ******"},\
        {"function": 'get_duration', "description": "FLOAT - duration"},\
        {"function": 'get_end_of_fade_in', "description": "FLOAT - end of fade in"},\
        {"function": 'get_energy', "description": "***** FLOAT - energy ******"},\
        {"function": 'get_key', "description": "INT - key"},\
        {"function": 'get_key_confidence', "description": "FLOAT - key confidence"},\
        {"function": 'get_loudness', "description": "FLOAT - loudness"},\
        {"function": 'get_mode', "description": "INT - mode"},\
        {"function": 'get_mode_confidence', "description": "FLOAT - mode confidence"},\
        {"function": 'get_start_of_fade_out', "description": "FLOAT - start of fade out"},\
        {"function": 'get_tempo', "description": "FLOAT - tempo"},\
        {"function": 'get_time_signature', "description": "INT - time signature"},\
        {"function": 'get_time_signature_confidence', "description": "FLOAT - time signature confidence"},\
        {"function": 'get_track_7digitalid', "description": "STRING - track id"},\
        {"function": 'get_segments_start', "description": "ARRAY FLOAT - segments start"},\
        {"function": 'get_segments_confidence', "description": "ARRAY FLOAT - segments confidence"},\
        {"function": 'get_segments_pitches', "description": "2D ARRAY FLOAT - segments pitches"},\
        {"function": 'get_segments_timbre', "description": "2D ARRAY FLOAT - segments timbre"},\
        {"function": 'get_segments_loudness_max', "description": "ARRAY FLOAT -  segments loudness max"},\
        {"function": 'get_segments_loudness_max_time', "description": "ARRAY FLOAT - segments loudness max time"},\
        {"function": 'get_segments_loudness_start', "description": "ARRAY FLOAT - segments loudness (max?) start"},\
        {"function": 'get_sections_start', "description": "ARRAY FLOAT - sections start"},\
        {"function": 'get_sections_confidence', "description": "ARRAY FLOAT - sections confidence"},\
        {"function": 'get_beats_start', "description": "ARRAY FLOAT - beats start"},\
        {"function": 'get_beats_confidence', "description": "ARRAY FLOAT - beats confidence"},\
        {"function": 'get_bars_start', "description": "ARRAY FLOAT - bars start"},\
        {"function": 'get_bars_confidence', "description": "ARRAY FLOAT - bars confidence"},\
        {"function": 'get_tatums_start', "description": "ARRAY FLOAT - tatums start"},\
        {"function": 'get_tatums_confidence', "description": "ARRAY FLOAT - tatums confidence"},\
        #{"function": 'get_artist_mbtags', "description": "ARRAY STRING - artist mbtags"},\
        #{"function": 'get_artist_mbtags_count', "description": "ARRAY INT - artist mbtags count"},\
        {"function": 'get_year', "description": "INT - year"}\
    ]
    return render_template('index.html',
        title = 'Home',
        rows = rows)

@app.route('/confirmQuery')
def confirmQuery():
    # Retrieve the parameters
    filename = request.args.get('filename', '')
    if filename == '':
        filename = 'Test'
    elementsRequested = request.args.getlist('fields')

    # Call the function to create the vector
    all_desired_data, all_desired_data_normalized = createDesiredVector(elementsRequested, filename)

    return render_template('confirmQuery.html',
        title = 'Requested Query',
        filename = filename,
        elementsRequested = elementsRequested,
        rawSamples = all_desired_data[:10],
        normSamples = all_desired_data_normalized[:10])

@app.route('/chooseClustering')
def chooseClustering():
    data_name = request.args.get('dataname', '')
    return render_template('chooseClustering.html',
        dataname = data_name)

@app.route('/clusterResult')
def getClustersResult():
    data_name = request.args.get('dataname', '')
    kmean_number = request.args.get('kmeannumber', '')
    if data_name == '':
        data_name = 'normOutputCleanTest.txt'
    data_path = './dump/' + data_name
    method = request.args.get('method', '')

    # Use the method send to clusterize the data
    if method == 'kmean':
        clusterList, barycentersList, infosList = kmeanTreatment(data_path, kmean_number)
    elif method == 'meanshift':
        clusterList, barycentersList, infosList = meanShiftTreatment(data_path)
    else:
        clusterList, barycentersList, infosList = kmeanTreatment(data_path, 4)

    clusterNumber = range(len(clusterList))
    cluster_mbtags = []
    for i in clusterNumber:
        artist_number = len(infosList[0][i])
        temp_dic = {}
        for k, v in infosList[2][i].iteritems():
            temp_dic[k] = format(float(v)*100 / artist_number, '.2f')
        cluster_mbtags.append(sorted(temp_dic.iteritems(), key=operator.itemgetter(1), reverse = True))

    # Make a dump of the results!
    with open('./cluster/' + method + data_name, 'wb') as f:
        cPickle.dump([clusterList, barycentersList, infosList], f)

    return render_template('clusteringresult.html', 
        datapath = data_path,
        method = method,
        clusterNumber = clusterNumber,
        clusterList = clusterList,
        barycentersList = barycentersList,
        infosList = infosList,
        mbtags_sorted = cluster_mbtags)

@app.route('/trackSearch')
def findTrack():
    track = request.args.get('song', '')
    artist = request.args.get('artist', '')
    if track == '' or artist == '':
        return render_template('tracksearch.html',
            searchOk = False)
    else:
        # Find the requested song with echonest API
        result = song.search(artist = artist, title = track)[0]

        return render_template('tracksearch.html',
            searchOk = True,
            result = result)

@app.route('/similarSong')
def findSimilarSong():
    path = './cluster/'
    # track = request.args.get('song', '')
    # artist = request.args.get('artist', '')
    # url = request.args.get('url', '')
    clusterfile = request.args.get('clusters', '')
    if clusterfile == '':
        ''' Define a default value !!'''
        clusterfile = 'kmeannormOutputCleanAdlen.txt'
        pass
    cluster_path = path + clusterfile
    # result = song.search(artist = artist, title = track)[0]
    # res = requests.get(url)
    # res_json = res.json()
    closest_center_number, song_vector, clusterList, barycentersList, infosList = findBestCluster(cluster_path)
    print closest_center_number
    # print song_vector
    # print clusterList
    # print barycentersList
    # print infosList

    # sorted_artists = OrderedDict(sorted(sorted_artists.items(), key=lambda t: -t[1]))
    sorted_artists = sorted(infosList[0][0].iteritems(), key=operator.itemgetter(1), reverse = True)
    print sorted_artists

    return render_template('similarsong.html', 
        closest_center_number = closest_center_number, 
        song_vector = song_vector,
        closest_center = barycentersList[closest_center_number],
        centers = barycentersList,
        centers_number = range(len(barycentersList)),
        similar_songs = infosList[1][closest_center_number],
        similar_artists = sorted_artists)