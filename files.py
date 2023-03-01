# Python program to read
# json file
  
  
import json
  
def read_json(Filename):
    # Opening JSON file
    f = open(Filename)
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Closing file
    f.close()

    return data

data = read_json("test.json")
print(data)