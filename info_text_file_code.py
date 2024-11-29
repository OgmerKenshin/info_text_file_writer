#import json again
#initiate the json file
#set up user input for IGN
#open and read json file
#search for the user input
# handle errors

file_path = "output.txt"
while True:
    search_ign = input("enter your IGN: ")


    searched = False
    with open(file_path, "r") as file:
        info = []
        for line in file:
          if line.startswith(f"IGN: {search_ign}"): 
                searched = True 
                info = [line]
                info.append(line)
          
          if searched and line.startswith(f"level: ")[1]:
                info.append(line)
                print("level found")

                
          if searched is True:
                 print(f"info on {search_ign}")
                 print(f"\n".join(info))
                 break
      
      




