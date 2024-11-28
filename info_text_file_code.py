#import json again
#initiate the json file
#set up user input for IGN
#open and read json file
#search for the user input
# handle errors
file_path = "output.txt"
with open(file_path, "w") as file:
      pass


while True:
      search_ign = ("enter your IGN: ").strip()


      searched = False
      with open(file_path, "r") as file:
            info = []
            for line in file:
                  line = line.strip()
                  if line.startswith("IGN:"):
                        if info and info[0] == f"IGN: {search_ign}":
                              searched = True
                              break
                        info = [line]


      
      




