import json

# Creating function to get the file I imported previously and parse it. 

def readJSON():
    try:
        with open('pokedex.json', 'r') as jsonFILE: #Reading the file
            data = json.load(jsonFILE) # Parsing the file
            print(json.dumps(data, indent=4)) # indenting so we have a clear object-like result 
            
            
        
    except FileNotFoundError:
        print('Sorry, file not found')

    


# Test: working ok
readJSON()






        