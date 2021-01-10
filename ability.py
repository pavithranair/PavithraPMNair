import requests

def ability(input_poke):
    ability_list = list()
    pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + input_poke).json()
    for ability in pokemon['abilities']:
        ability_list.append(ability['ability']['name'])
    return(ability_list)


