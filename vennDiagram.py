import spotipy
import spotipy.util as util

def write_tracks(tracks, f):
    print len(tracks['items'])
    for i, item in enumerate(tracks['items']):
        track = item['track']
        f.write(("   %d %32.32s %s\n" % (i, track['artists'][0]['name'], track['name'])).encode('utf8'))
        print("   %d %32.32s " % (i, track['artists'][0]['name'], track['name']))
    f.close()

def create_arrays(tracks1, tracks2):
    first_array=[]
    second_array=[]
    duplicate_array=[]
    for item in tracks1['items']:
        track = item['track']
        first_array.append("    %32.32s %s" % (track['artists'][0]['name'], track['name']))

    for item in tracks2['items']:
        track = item['track']
        name = ("    %32.32s %s" % (track['artists'][0]['name'], track['name']))
        if name in first_array:
            first_array.remove(name)
            duplicate_array.append(name)
        else:
            second_array.append(name)
    return (first_array,second_array,duplicate_array)








scope = 'user-library-read'
username = '1159991532'

token = util.prompt_for_user_token(username, scope)


spotify = spotipy.Spotify(auth=token)
dylan = '1159991532'
megan = 'petrichortardis'
dank_tunes = '14VcSdE3lgDQYuXA6GzpHU'
september = '1cHxarRhQFiANkZE3ZZiy5'
shooters = '03qWzXsDfZoyGAhFQJwTp2'
results1 = spotify.user_playlist(dylan, dank_tunes, fields = "tracks")
tracks1 = results1['tracks']
results2 = spotify.user_playlist(dylan, shooters, fields = "tracks")
tracks2 = results2['tracks']
sets = create_arrays(tracks1, tracks2)

print "DUPLICATES"
for x in sets[2]:
    print x
print "LIST 1"
for x in sets[0]:
    print x
print "LIST 2"
for x in sets[1]:
    print x
