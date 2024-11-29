#pseudo code
#set a dictionary 
#Set while loops for multiple inputs
#set try and except for input errors
#put in the user input statements
#place the input info in a dictionary for each person
#write output in a textfile



person = {}
file_path = "output.txt"
while True:
    while True:
        try:
            IGN = input("enter your in game name: ")
            level = int(input("enter your level: "))
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
                "rank" : rank
                
            }

            with open(file_path, "a") as file_handler:
                file_handler.write(f"IGN: {IGN}\n")
                file_handler.write(f"level: {level}\n")
                file_handler.write(f"MLID: {MLID}\n")
                file_handler.write(f"server: {server}\n")
                file_handler.write(f"guardian: {guardian}\n")
                file_handler.write(f"rank: {rank}\n")
                print("\n")
        
        
        
            print("your input has been saved as txt file, welcome to mobile legends")
            break
        except:
            print("wrong input, please enter again")
            break
    try:
        retry = input("do you wanna input again? y/n: " )
        if retry == "n":
            print("ok")
            break
        else: 
            continue
    except:
        print("invalid, y/n only.")
    

    
