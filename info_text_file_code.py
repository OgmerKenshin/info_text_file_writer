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
        for i, line in file:
          if line.startswith(f"IGN: {search_ign}"): 
                searched = True 
                info = [line]
                info.append(line)
          for k in range(i +1, len(line)):
               if line[k].startswith("IGN:"): 
                   break
               info.append(line[k])
               break

                
          if searched is True:
                 print(f"info on {search_ign}")
                 print(f"\n".join(info))
                 break
      
      




