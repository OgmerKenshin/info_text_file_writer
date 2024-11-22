#import json again
#initiate the json file
#set up user input for IGN
#open and read json file
#search for the user input
# handle errors

import json

file_hold = "output.json"

IGN_input = input("enter your in game name: ")
try:
     with open(file_hold, "r") as file:
        info = json.load(file)
        print("info is loaded now")

except FileNotFoundError:
    print("file not found, creating new file")
    info = {}
    with open (file_hold, "w") as file:
        json.dump(info, file)

except json.JSONDecodeError:
    with open(file_hold, "w") as file: 
        json.dump(info, file)



    

