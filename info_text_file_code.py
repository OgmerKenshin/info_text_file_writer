#import json again
#initiate the json file
#set up user input for IGN
#open and read json file
#search for the user input
# handle errors

file_path = "output.txt"


info = []
info_dict = {}


with open(file_path, "r") as file:
      current_ign = None

      for line in file:
         line = line.strip()

         if line.startswith("IGN:"): 
            current_ign = line.split(": ")[1]
            info_dict[current_ign] = [line]

         elif current_ign:
            info_dict[current_ign].append(line)


while True:        
      while True:
             try: 
                search_ign = input("IGN please: ")
                
                if search_ign.lower() in info_dict:
                 print(f"info on {search_ign}")
                 print(f"\n".join(info_dict[search_ign]))
                 break
       
            
                else:
                  print(f"no info for {search_ign}")
                  break
         
             except:
               print("wrong input, try again.")
               break
      try:
        retry = input("do you wanna input again? y/n: " )
        if retry == "n":
            print("maybe another day then")
            break
        else: 
            continue
      except:
         print("invalid, y/n only.")
         break
         

       
            
               
      
      




