import requests
import requests.structures

def pokemons(pokomon="pikachu"):
    search = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokomon}")
    print("isim: "+str(search.json()["name"])+" kilo: "+str(search.json()["weight"]))
try:
    which_pokemon = input("hangi pokemonu istiyorsunuz: ")
    pokemons(which_pokemon)
except:
    print("hata var")