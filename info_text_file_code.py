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
        lines = file.readlines()
        info = []

        for i, line in enumerate(lines):
          if line.startswith(f"IGN: {search_ign}"): 
                searched = True
                info.append(lines)

                for subsequent_line in lines[i + 1:]:
                     if subsequent_line.startswith("IGN:"):
                          break
                     info.append(subsequent_line)

        
      
            

                
          if searched == True:
            print(f"info on {search_ign}")
            print(f"\n".join(info))
            break
          else:
            print(f"no info for {search_ign}")
            break
               
      
      




