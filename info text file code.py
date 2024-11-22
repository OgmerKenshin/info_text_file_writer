#pseudo code
#set a dictionary 
#Set while loops for multiple inputs
#set try and except for input errors
#put in the user input statements
#place the input info in a dictionary for each person
#write output in a textfile
import json


person = {}
file_hold = "output.json"
while True:
    while True:
        try:
            IGN = input("enter your in game name: ")
            level = int(input("enter your age: "))
            MLID = (input("enter your account ID: "))
            server = input("enter your server: ")
            guardian = input("enter name of guardian: ")
            role = input("enter your role: ")
            rank = input("what is your current rank: ")

            if len(MLID) != 10: 
                print("number must be 10 digits")
                False
            
            person[IGN] = {
                "IGN" : IGN,
                "level" : level,
                "MLID" : MLID,
                "server" : server,
                "guardian" : guardian,
                "role" : role,
                "rank" : rank
                
            }

            with open(file_hold, "a") as file_handler:
                json.dump(person, file_handler, indent=4)
        

            print("your input has been saved as json file, welcome to mobile legends")
        except:
            print("wrong input, please enter again")
        break
    break

    
