temp_output = ""
isFinished = False

def dinnerEntry():
    val = input("Please enter you dinner item: ")
    return val
    
while not isFinished:
    strValue = dinnerEntry()
    with open("text_files/dinner_menu.txt","a") as dinner_txt:
        dinner_txt.write(strValue + "\n")
        
    strFinished = input("Do you want to continue? Yes or No: ")
    if strFinished == "Yes" or strFinished == "Y":
        continue
    else:
        isFinished = True        

            