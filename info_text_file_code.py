#import json again
#initiate the json file
#set up user input for IGN
#open and read json file
#search for the user input
# handle errors
import json
file_path = "output.json"
with open(file_path, "w") as file:
      pass



with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()
        data = json.loads(contents)
        print("file read")
        
while True: 
      search_IGN = input("enter your in game name: ")
      searched = None
      for key, value in data.items():
             if value.get("IGN") == search_IGN:
                    found = value
                    break
      
      if found:
             print(f"IGN found, hello: {json.dumps(found, indent= 4)}")
      else:
             print("IGN not registered yet")



