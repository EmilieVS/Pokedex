import json

#This is a fully commented version of the code for learning or futur improvement(if I have to get back to it when practicing) 

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
        

#sortPokemon()
#This function is useless as it works only for the first pokemon. Have ot think it through...
# def nextEvolution(pokemon):
#           for pokemon in pokeData['pokemon']:
#             #pokemon = pokeData['pokemon'][0]['name']
#             pokemon = pokemon['name']
#             evolution = pokeData['pokemon'][0]['next_evolution']
#           print(pokemon)

# nextEvolution('Charmander')


#Last thing is to get a pokemon evolution based on his name. 
#With 151 of them in the list, it is better to make use of classes ! Let's ma ke a Pokemon class based on the data inside the JSON so I can make pokemon for each one in the file
#Let's make a Pokemon class that will return the data I want. 

class Pokemon:
     def __init__(self,pokeData):
          self.id = pokeData.get('id')
          self.num = pokeData.get('num')
          self.name = pokeData.get('name')
          self.img = pokeData.get('img') 
          self.type = pokeData.get('type') 
          self.height = pokeData.get('height') 
          self.weight = pokeData.get('weight') 
          self.candy = pokeData.get('candy') 
          self.candy_count = pokeData.get('candy_count') 
          self.egg = pokeData.get('egg') 
          self.spawn_chance = pokeData.get('spawn_chance') 
          self.avg_spawns = pokeData.get('avg_spawns') 
          self.spawn_time = pokeData.get('spawn_time') 
          self.multipliers = pokeData.get('multipliers') 
          self.weaknesses = pokeData.get('weaknesses') 
          self.next_evolution = pokeData.get('next_evolution') 
     
     def nextEvolution(self): 
      if self.next_evolution :
        name = []
        for evolution in self.next_evolution:
             name.append(evolution['name'])
        return ", ".join(name)
      else : 
           return None



#Now creating the pokemon and getting only the data I want (evolution)
def pokedex():
     for pokemon in pokeData['pokemon']:
          newPokemon = Pokemon(pokemon)
          evolution = newPokemon.nextEvolution()
          
          if evolution :
           print(f"{newPokemon.name} évolue en {newPokemon.nextEvolution()}")

          elif evolution == None:
               print(f"{newPokemon.name} n'a pas d'évolution")

pokedex()