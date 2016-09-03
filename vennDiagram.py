import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = '1159991532'

token = util.prompt_for_user_token(username, scope)


spotify = spotipy.Spotify(auth=token)
username = '1159991532'
playlist1 = '14VcSdE3lgDQYuXA6GzpHU'
results = spotify.user_playlist(username, playlist1, fields = "tracks")
