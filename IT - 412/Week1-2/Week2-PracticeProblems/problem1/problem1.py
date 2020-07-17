temp_output = ""
with open("text_files\movie_list.txt") as txt_file:
    for strmovie in txt_file:
        temp_output = temp_output + strmovie
    
with open("text_files/output.txt", "w") as file_output:
    file_output.write(temp_output)
            
            
     