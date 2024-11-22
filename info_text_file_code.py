#import json again
#initiate the json file
#set up user input for IGN
#open and read json file
#search for the user input
# handle errors

import json

file_hold = "output.json"

IGN = input("enter your in game name: ")

try: 
    with open(file_hold, "r") as file:
        info = json.load(file)



except: