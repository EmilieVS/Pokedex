import json

# Creating function to get the file I imported previously and parse it. 
def readJSON():
    try:
        with open('pokedex.json', 'r') as jsonFILE: 
            data = json.load(jsonFILE) 
            
            return data
    
    except FileNotFoundError:
        print('Sorry, file not found')

pokeData = readJSON()  

# function to count the number of Pokemon
def countPokemon():
            numOfPokemon = len(pokeData['pokemon']) 
            print(f"Il y a {numOfPokemon} Pokémons dans le Pokédex")
            

#Exercice wants me to do the same function but using a loop
def countLoopPokemon():
            count = 0
            for id in pokeData['pokemon']:
                count+=1
               
            print(f"Il y a {count} Pokémons")


# Function to count Pokemons over 10kg
def pokemonsWeight():
    count = 0

    for pokemon in pokeData['pokemon']:
        weight = pokemon['weight']
        pokeWeight = float(weight.replace("kg",''))
      
        if pokeWeight > 10.0:
            count+=1

    print(f"Il y a {count} Pokémons qui pèsent plus de 10 kg")

#Function to sort them by weight
def sortPokemon():
    pokeData['pokemon'].sort(key = lambda pokemon:float(pokemon['weight'].replace("kg",'')))
      
    for pokemon in pokeData['pokemon']:
         print(f"{pokemon['name']} : {pokemon['weight']}")

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
        return " puis ".join(name)
      else : 
           return None


#Creating(/instanciating) a pokemon object for each one in the JSON
def pokedex():
     for pokemon in pokeData['pokemon']:
          newPokemon = Pokemon(pokemon)
          evolution = newPokemon.nextEvolution()
          
          if evolution :
           print(f"{newPokemon.name} évolue en {newPokemon.nextEvolution()}")

          elif evolution == None:
               print(f"{newPokemon.name} n'a pas d'évolution")

pokedex()