import spotipy
import spotipy.util as util

def write_tracks(tracks, f):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        f.write(("   %d %32.32s %s\n" % (i, track['artists'][0]['name'], track['name'])).encode('utf8'))
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))
    f.close()

scope = 'user-library-read'
username = '1159991532'

token = util.prompt_for_user_token(username, scope)


spotify = spotipy.Spotify(auth=token)
username1 = '1159991532'
username2 = 'petrichortardis'
playlist1 = '14VcSdE3lgDQYuXA6GzpHU'
playlist2 = '1cHxarRhQFiANkZE3ZZiy5'
results = spotify.user_playlist(username2, playlist2, fields = "tracks, next")
tracks = results['tracks']
with open('out.txt', 'wb') as f:
    write_tracks(tracks, f)
