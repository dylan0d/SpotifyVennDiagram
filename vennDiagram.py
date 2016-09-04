import spotipy
import spotipy.util as util

def print_array(tracks):
    for x in tracks:
        print x

def print_results(sets):
    print "DUPLICATES"
    print_array(sets[2])
    print "LIST 1"
    print_array(sets[0])
    print "LIST 2"
    print_array(sets[1])

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

if __name__ == "__main__":
    scope = 'user-library-read'
    username = '1159991532'

    token = util.prompt_for_user_token(username, scope)


    spotify = spotipy.Spotify(auth=token)
    dylan = '1159991532'
    megan = 'petrichortardis'
    conor = '1159991532'
    dank_tunes = '14VcSdE3lgDQYuXA6GzpHU'
    september = '1cHxarRhQFiANkZE3ZZiy5'
    shooters = '03qWzXsDfZoyGAhFQJwTp2'
    zombies2 = '3GGlANCZ2Kb4JOWsoRsSRO'
    results1 = spotify.user_playlist(conor, zombies2, fields = "tracks")
    tracks1 = results1['tracks']
    results2 = spotify.user_playlist(dylan, shooters, fields = "tracks")
    tracks2 = results2['tracks']
    sets = create_arrays(tracks1, tracks2)

    print_results(sets)
