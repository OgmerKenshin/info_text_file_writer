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
          line= line.strip()

          if line.startswith(f"IGN: ") and not line.startswith(f"IGN: "): 
                searched = True
                info.append(line.strip())

                for subsequent_line in lines[i + 1:]:
                     if subsequent_line.startswith("IGN:"):
                          break
                     info.append(subsequent_line.strip())

        
      
                
          if searched == True:
            print(f"info on {search_ign}")
            print(f"\n".join(info))
            
          else:
            print(f"no info for {search_ign}")
            
               
      
      




