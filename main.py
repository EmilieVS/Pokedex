import json

# Creating function to get the file I imported previously and parse it. 

def readJSON():
    try:
        with open('pokedex.json', 'r') as jsonFILE: #Reading the file
            data = json.load(jsonFILE) # Parsing the file
            print(json.dumps(data, indent=4)) # indenting so we have a clear object-like result 
            
            
        
    except FileNotFoundError:
        print('Sorry, file not found')

    
#readJSON()

# function to count the number of Pokemon
def countPokemon():
    with open('pokedex.json', 'r') as jsonFILE:
            data = json.load(jsonFILE) 
            #print(json.dumps(data, indent=4))
            numOfPokemon = len(data['pokemon']) # len function to get the number of element
            print(f"Il ya {numOfPokemon} Pokémons dans le pokédex")
            

#countPokemon()

#Exercice wants me to do the same function but using a loop

def countLoopPokemon():
     with open('pokedex.json', 'r') as jsonFILE:
            data = json.load(jsonFILE)
            count = 0
            for id in data['pokemon']:
                count+=1
               
            print(f"Il y a {count} Pokémons")


countLoopPokemon()



        