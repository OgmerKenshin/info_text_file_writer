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

    for IGN in info:
        if IGN_input == info[IGN]:




except: