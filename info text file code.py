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
            name = input("enter your name: ")
            age = int(input("enter your age: "))
            number = int(input("enter your number: "))
            address = input("enter your address: ")
            guardian = input("any parents or close relatives?: ")

            if len(number) != 11: 
                print("number must be 11 digits")
                False
            
            person[name] = {
                "name" : name,
                "age" : age,
                "number" : number,
                "address" : address,
                "guardian" : guardian
            }

            with open("C:\\Users\\kensh\\OneDrive - DepEd-NCR\\coding assignment text file", "a") as file_handler:
                file_handler.write(person)

            print("your input has been saved")
            break
        except:
            print("wrong input")
