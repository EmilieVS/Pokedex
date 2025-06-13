import json

def readJSON():
    try:
        with open('pokedex.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)
        
    except FileNotFoundError:
        print('Sorry, file not found')
    

readJSON()


        