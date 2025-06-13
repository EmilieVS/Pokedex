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
            
#countPokemon()

#Exercice wants me to do the same function but using a loop
def countLoopPokemon():
            count = 0
            for id in pokeData['pokemon']:
                count+=1
               
            print(f"Il y a {count} Pokémons")


#countLoopPokemon()

# Function to count Pokemons over 10kg
def pokemonsWeight():
    count = 0

    for pokemon in pokeData['pokemon']:
        weight = pokemon['weight']
        pokeWeight = float(weight.replace("kg",''))
      
        if pokeWeight > 10.0:
            count+=1

    print(f"Il y a {count} Pokémons qui pèsent plus de 10 kg")


#pokemonsWeight()


#Function to sort them by weight
def sortPokemon():
#getting the list sorted : "key" works with functions only so using lambda(anonymous function)
    pokeData['pokemon'].sort(key = lambda pokemon:float(pokemon['weight'].replace("kg",'')))
      
    for pokemon in pokeData['pokemon']:
         print(f"{pokemon['name']} : {pokemon['weight']}")
        

sortPokemon()