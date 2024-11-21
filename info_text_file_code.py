#pseudo code
#set a dictionary 
#Set while loops for multiple inputs
#set try and except for input errors
#put in the user input statements
#place the input info in a dictionary for each person
#write output in a textfile
import json

data = "list of players"
file_hold = "output.json"

with open(file_hold, "w") as file:
    file.write(data)
    print("output dile initialized")