import sys
import spotipy
import spotipy.util as util
from Tkinter import *


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

def make_string(arr):
    str = ""
    if len(arr)>27:
        for x in range(27):
            str+=arr[x]+"\n"
        str+="And even more in the terminal"
    else:
        for x in arr:
            str+= x+"\n"
    return str

def extract_duplicates(tracks1, tracks2):
    first_array=[]
    second_array=[]
    duplicate_array=[]
    for item in tracks1['items']:
        track = item['track']
        #%32.32s
        first_array.append("%s %s" % (track['artists'][0]['name'], track['name']))

    for item in tracks2['items']:
        track = item['track']
        name = ("%s %s" % (track['artists'][0]['name'], track['name']))
        if name in first_array:
            first_array.remove(name)
            duplicate_array.append(name)
        else:
            second_array.append(name)

    return (first_array,second_array,duplicate_array)

if __name__ == "__main__":
    scope = 'playlist-read-private'
    username = '1159991532'#raw_input("Please enter your Spotify username: ")
    #username = '1159991532'

    token = util.prompt_for_user_token(username, scope, '1c5ec05f1b9b4cbab72f6bd0e5cb1d94', '6355c38a9bf9415c98d0217a5a9b0b89',
'https://github.com/dylan0d/SpotifyVennDiagram')


    spotify = spotipy.Spotify(auth=token)

    #user1 = raw_input("Username of owner of the 1st playlist: ")
    #playlist1 = raw_input("URI of 1st playlist: ")
    #user2 = raw_input("Username of owner of the 2nd playlist: ")
    #playlist2 = raw_input("URI of 2nd playlist: ")

    results1 = spotify.user_playlist('1159991532', '14VcSdE3lgDQYuXA6GzpHU', fields = "tracks")
    tracks1 = results1['tracks']
    results2 = spotify.user_playlist('1159991532', '03qWzXsDfZoyGAhFQJwTp2', fields = "tracks")
    tracks2 = results2['tracks']

    sets = extract_duplicates(tracks1, tracks2)
    list1 = make_string(sets[0])
    list2 = make_string(sets[1])
    list3 = make_string(sets[2])
    print_results(sets)
#sets calculated, now to output them graphically
    root = Tk()

    canvas_width=1300
    canvas_height=root.winfo_screenheight() - 100
    canvas=Canvas(root, width = canvas_width, height=canvas_height)
    #topx, topy, bottomx, bottomy
    #top left corner = 0,0
    canvas.create_oval(canvas_width/16, 10, (11*canvas_width)/16, canvas_height-10, fill="green", width=2)
    canvas.create_oval((5*canvas_width)/16, 10, (15*canvas_width/16), canvas_height-10, outline="blue", fill="orange", width=2)
    canvas.create_oval(canvas_width/16, 10, (11*canvas_width)/16, canvas_height-10, outline="red", width=2)
    canvas_id = canvas.create_text(200, 100, anchor="nw")
    canvas_id2 = canvas.create_text(600, 100, anchor = "nw")

    canvas.pack()

    canvas.itemconfig(canvas_id, text=list1)
    canvas.itemconfig(canvas_id2, text=list2)

    mainloop()
    print "Exited successfully"


'''    dylan = '1159991532'
    megan = 'petrichortardis'
    conor = '1159991532'
    dank_tunes = '14VcSdE3lgDQYuXA6GzpHU'
    september = '1cHxarRhQFiANkZE3ZZiy5'
    shooters = '03qWzXsDfZoyGAhFQJwTp2'
    zombies2 = '3GGlANCZ2Kb4JOWsoRsSRO'''
