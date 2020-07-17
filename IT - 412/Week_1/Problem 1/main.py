from functions import *

"""Main method that displays the song and artist title
"""

playlist = []
validEntry = True

while validEntry:
    key = 0
    checkedName = False
    while not checkedName:
        artist_name = input("Please enter the Artist name: ")
        if artist_name == "":
            print("Invalid Entry - artist name is missing.")
            checkedName = False 
            break

        if not str(artist_name):
            print("Artist Name is not a string")
            checkName = False 
        else: 
            checkedName = True

    if checkedName== False:
        validEntry == False


    checkedSong = False
    while not checkedSong:
        song_name = input("Please enter the Song name: ")
        if song_name == "":
            print("Invalid Entry - artist name is missing.")
            checkedSong = False 
            

        if not str(song_name):
            print("Song Name is not a string.")
            checkSong = False 
        else: 
            checkedSong = True

        #Checks for a valid entry and breaks when entry is invalid
        if checkedSong == False:
            validEntry = False

        song = {}
       
        song.setdefault(key,{'Artist': artist_name, 'Title': song_name})
        key = key + 1
        playlist.append(song.copy())
            
    add_another_song = input("Do you wish to add another song? Please enter a Y for YES or N for NO?")

    if add_another_song.upper() == "N":
        print_song_information(playlist)
        break
    else:
        continue