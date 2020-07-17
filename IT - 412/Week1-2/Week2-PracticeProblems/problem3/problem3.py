import os.path
import shutil

temp_output = ""
if os.path.exists("text_files/output.txt") or os.path.exists("text_files/output.txt"):
    with open("text_files\movie_list.txt") as txt_file:
        for movie in txt_file:
            strmovie = movie.strip()        
            temp_output = temp_output + strmovie
else:
    pass

    
            
            
     