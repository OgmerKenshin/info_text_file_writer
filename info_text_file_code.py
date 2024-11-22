#import json again
#initiate the json file
#set up user input for IGN
#open and read json file
#search for the user input
# handle errors

file_path = "output.json"
with open(file_path, "w") as file:
      pass


import json


IGN_input = input("enter your in game name: ")

with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)


info = json.loads(contents)
print("json file loaded success")

