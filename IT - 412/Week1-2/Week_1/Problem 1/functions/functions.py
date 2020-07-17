def song_information(artist, title):
    """Takes a an artist and song title with validation
    
    Arguments:
        artist {string} -- Artist Name
        title {string} -- Song title by Artist
    
    Returns:
        Dictionary -- Song and artist title in a dictionary
    """
    song_detail = {}

    result_ok = True        
    try:
        artist = str(artist)
    except:
        print("Song is not a string")
        result_ok = False

    try:
        title = str(title)
    except:
        print("Artist is not a string")
        result_ok = False

    if result_ok:
        song_detail ={"artist_name": artist, "song_title": title}

    return song_detail



def print_song_information(list):
    for dictionary in list:
        for key, value in dictionary.items():
            information = "Artist Name: {0} | Song Title: {1}".format (value["Artist"],value["Title"])
            print(information) 