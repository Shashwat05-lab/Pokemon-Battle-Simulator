from pokemon_battle import PokemonBattleAPI

# Initialize the API
battle_api = PokemonBattleAPI()

# Load Pokémon data from CSV file
battle_api.load_pokemons('Requirement\\pokemon.csv')

# List available Pokémon (pagination example)
print(battle_api.get_pokemons(page=1, per_page=10))

# Start a battle between two Pokémon
battle_id = battle_api.start_battle('Pikachu', 'Charizard')
if battle_id:
    print(f"Battle started with ID: {battle_id}")

    # Get the status of the battle
    status = battle_api.get_battle_status(battle_id)
    
    print(status)
    print(f'Battle Status : ',status.get('status'))
    print(f'Result : ',status.get('result').get('winnerName'))
    print(f'Won By : ',status.get('result').get('wonByMargin'))

else:
    print("Pokémon not found or spelling error.")