#pseudo code
#set a dictionary 
#Set while loops for multiple inputs
#set try and except for input errors
#put in the user input statements
#place the input info in a dictionary for each person
#write output in a textfile

person = {}

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
                continue
            
            person[IGN] = {
                "IGN" : IGN,
                "level" : level,
                "MLID" : MLID,
                "server" : server,
                "guardian" : guardian,
                "role" : role,
                "rank" : rank
                
            }

            with open("c:\\Users\\kensh\\OneDrive - DepEd-NCR\\coding assignment text file\\text_file.py", "a") as file_handler:
                file_handler.write("\n" + str(person[IGN]))
        

            print("your input has been saved, welcome to mobile legends")
            break

        except ValueError:
            print("wrong input, please enter again")
    
