#import json again
#initiate the json file
#set up user input for IGN
#open and read json file
#search for the user input
# handle errors
info_dictionary = {}
file_path = "output.txt"
while True:
    search_ign = input("enter your IGN: ")


    searched = False
    with open(file_path, "r") as file:
        lines = file.readlines()
        info = []

        for i, line in enumerate(lines):
          line= line.strip()

          if line.startswith(f"IGN:"): 
                if info:
                    ign = info[0].split(": ")[1]
                    info_dictionary[ign] = info
                info = [line]
                    
                
                
        
      
                
          if searched == True:
            print(f"info on {search_ign}")
            print(f"\n".join(info))
            
          else:
            print(f"no info for {search_ign}")
            
               
      
      




