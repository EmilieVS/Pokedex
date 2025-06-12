import requests

jsonURL = ('https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json')
response = requests.get(jsonURL)
data = response.json()


def getPokemon():
    print(data)


getPokemon()


        