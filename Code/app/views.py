from flask import render_template, request
from app import app
from createVectorCluster import createDesiredVector

@app.route('/')
@app.route('/index')
def index():
    rows = \
    [\
        {"function": 'get_artist_familiarity', "description": "artist familiarity"},\
        {"function": 'get_artist_hotttnesss', "description": "artist hotttnesss"},\
        {"function": 'get_artist_id', "description": "artist id"},\
        {"function": 'get_artist_mbid', "description": "artist mbid"},\
        {"function": 'get_artist_playmeid', "description": "artist playmeid"},\
        {"function": 'get_artist_7digitalid', "description": "artist 7digitalid"},\
        {"function": 'get_artist_latitude', "description": "artist latitude"},\
        {"function": 'get_artist_longitude', "description": "artist longitude"},\
        {"function": 'get_artist_location', "description": "artist location"},\
        {"function": 'get_artist_name', "description": "artist name"},\
        {"function": 'get_release', "description": "release"},\
        {"function": 'get_release_7digitalid', "description": "release 7digitalid"},\
        {"function": 'get_song_id', "description": "song id"},\
        {"function": 'get_song_hotttnesss', "description": "song hotttnesss"},\
        {"function": 'get_title', "description": "title"},\
        {"function": 'get_track_7digitalid', "description": "track 7digitalid"},\
        {"function": 'get_similar_artists', "description": "similar artists"},\
        {"function": 'get_artist_terms', "description": "artist terms"},\
        {"function": 'get_artist_terms_freq', "description": "artist terms freq"},\
        {"function": 'get_artist_terms_weight', "description": "artist terms weight"},\
        {"function": 'get_analysis_sample_rate', "description": "analysis sample rate"},\
        {"function": 'get_audio_md5', "description": "audio md5"},\
        {"function": 'get_danceability', "description": "danceability"},\
        {"function": 'get_duration', "description": "duration"},\
        {"function": 'get_end_of_fade_in', "description": "end of fade in"},\
        {"function": 'get_energy', "description": "energy"},\
        {"function": 'get_key', "description": "key"},\
        {"function": 'get_key_confidence', "description": "key confidence"},\
        {"function": 'get_loudness', "description": "loudness"},\
        {"function": 'get_mode', "description": "mode"},\
        {"function": 'get_mode_confidence', "description": "mode confidence"},\
        {"function": 'get_start_of_fade_out', "description": "start of fade out"},\
        {"function": 'get_tempo', "description": "tempo"},\
        {"function": 'get_time_signature', "description": "time signature"},\
        {"function": 'get_time_signature_confidence', "description": "time signature confidence"},\
        {"function": 'get_track_id', "description": "track id"},\
        {"function": 'get_segments_start', "description": "segments start"},\
        {"function": 'get_segments_confidence', "description": "segments confidence"},\
        {"function": 'get_segments_pitches', "description": "segments pitches"},\
        {"function": 'get_segments_timbre', "description": "segments timbre"},\
        {"function": 'get_segments_loudness_max', "description": "segments loudness max"},\
        {"function": 'get_segments_loudness_max_time', "description": "segments loudness max time"},\
        {"function": 'get_segments_loudness_start', "description": "segments loudness start"},\
        {"function": 'get_sections_start', "description": "sections start"},\
        {"function": 'get_sections_confidence', "description": "sections confidence"},\
        {"function": 'get_beats_start', "description": "beats start"},\
        {"function": 'get_beats_confidence', "description": "beats confidence"},\
        {"function": 'get_bars_start', "description": "bars start"},\
        {"function": 'get_bars_confidence', "description": "bars confidence"},\
        {"function": 'get_tatums_start', "description": "tatums start"},\
        {"function": 'get_tatums_confidence', "description": "tatums confidence"},\
        {"function": 'get_artist_mbtags', "description": "artist mbtags"},\
        {"function": 'get_artist_mbtags_count', "description": "artist mbtags count"},\
        {"function": 'get_year', "description": "year"}\
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
    createDesiredVector(elementsRequested, filename)

    return render_template('confirmQuery.html',
        title = 'Requested Query',
        filename = filename,
        elementsRequested = elementsRequested,
        computationEnded = True)