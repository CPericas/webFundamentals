import requests
import json

#TASK 1
#response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
#json_data = response.text

#pikachu_data = json.loads(json_data)

#print(pikachu_data["name"])
#print(pikachu_data["abilities"])

#TASK 2
def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name']
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        weight = data['weight']
        return name, abilities, weight
    else:
        print(f"Failed to get data for {pokemon_name}. Status code: {response.status_code}")
        return None, None, None

def print_pokemon_info(name, abilities, weight):
    if name and abilities and weight is not None:
        print(f"Pokémon: {name.capitalize()}")
        print("Abilities:")
        for ability in abilities:
            print(f" - {ability.capitalize()}")
        print(f"Weight: {weight / 10} kg")
        print()

pokemon_list = ['pikachu', 'charmander', 'bulbasaur']

total_weight = 0
pokemon_count = 0
for pokemon in pokemon_list:
    name, abilities, weight = get_pokemon_info(pokemon)
    if weight is not None:
        total_weight += weight
        pokemon_count += 1
    print_pokemon_info(name, abilities, weight)

if pokemon_count > 0:
    average_weight = total_weight / pokemon_count / 10  
    print(f"Average Weight of the chosen Pokémon: {average_weight:.2f} kg")
