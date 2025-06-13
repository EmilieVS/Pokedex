import json

# Creating function to get the file I imported previously and parse it. 

def readJSON():
    try:
        with open('pokedex.json', 'r') as jsonFILE: #Reading the file
            data = json.load(jsonFILE) # Parsing the file
            #print(json.dumps(data, indent=4)) # indenting so we have a clear object-like result 
            return data
            
        
    except FileNotFoundError:
        print('Sorry, file not found')


pokeData = readJSON()  


# function to count the number of Pokemon
def countPokemon():

            numOfPokemon = len(pokeData['pokemon']) # len function to get the number of element
            print(f"Il ya {numOfPokemon} Pokémons dans le Pokédex")
            

countPokemon()

#Exercice wants me to do the same function but using a loop

def countLoopPokemon():
            count = 0
            for id in pokeData['pokemon']:
                count+=1
               
            print(f"Il y a {count} Pokémons")


#countLoopPokemon()


    


        