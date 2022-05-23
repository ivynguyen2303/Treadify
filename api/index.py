from http.server import BaseHTTPRequestHandler #imported to have an http endpoint
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
# pylint: disable-all

def generate_playlist(artistName):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="97b6ecab3a584348b32658e0a3d38aab",
                                                           client_secret="af301e528ce540d080a8d92a5b6718f5"))
    
    results = sp.search(artistName, limit=20)

    tempoDict = {}
    innerdict = {}

    for idx, track in enumerate(results['tracks']['items']):
        tempoDict[track['name']] = sp.audio_features(track['id'])[0]['tempo']
        #innerdict[sp.audio_features(track['id'])[0]['tempo']] = [sp.audio_features(track['id'])[0]['tempo']]/40
        #print(sp.audio_features(track['id'])[0]['tempo'])
        #print(idx, track['name'])

    scope = "user-library-read"
    sortedTracks= sorted(tempoDict.items(), key=operator.itemgetter(1))
    final = []
    for x in range(len(sortedTracks)):
        final.append((sortedTracks[x][0], sortedTracks[x][1],(sortedTracks[x][1]/40)))

    print(final)
    
    #sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return json.dumps(final)

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        artist_name = re.match(r"/api/generate/([a-z]+)", self.path).groups()[0]
        # self.path stuff
        # /api/generate/api/artist_name
        # data = generate_playlist(artist_name)
        data = generate_playlist(artist_name)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(data.encode())