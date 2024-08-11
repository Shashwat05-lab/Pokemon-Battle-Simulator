import csv
import difflib
from pokemon import Pokemon
from battle import Battle
from concurrent.futures import ThreadPoolExecutor

class PokemonBattleAPI:
    def __init__(self):
        self.pokemons = {}
        self.battles = {}
        self.executor = ThreadPoolExecutor(max_workers=4)  # Configure thread pool

    def load_pokemons(self, csv_file_path: str):
        with open(csv_file_path, newline='', errors = 'ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name'].lower()
                type1 = row['type1'].lower()
                type2 = row['type2'].lower() if row['type2'] else ''
                attack = int(row['attack'])
                against = {key.replace('against_', ''): float(value) for key, value in row.items() if key.startswith('against_')}
                self.pokemons[name] = Pokemon(name, type1, type2, attack, against)

    def get_pokemons(self, page: int = 1, per_page: int = 10):
        start = (page - 1) * per_page
        end = start + per_page
        return list(self.pokemons.keys())[start:end]

    def start_battle(self, name_a: str, name_b: str):
        name_a = difflib.get_close_matches(name_a.lower(), self.pokemons, n=1, cutoff=0.8)
        name_b = difflib.get_close_matches(name_b.lower(), self.pokemons, n=1, cutoff=0.8)
        if not name_a or not name_b or name_a[0] not in self.pokemons or name_b[0] not in self.pokemons:
            return None

        pokemon_a = self.pokemons[name_a[0]]
        pokemon_b = self.pokemons[name_b[0]]
        battle = Battle(pokemon_a, pokemon_b)
        self.battles[battle.battle_id] = battle
        
        # Start the battle asynchronously
        self.executor.submit(self._run_battle, battle)
        return battle.battle_id
    
    def _run_battle(self, battle: Battle):
        try:
            battle.start()
        except Exception as e:
            battle.status = "BATTLE_FAILED"
            battle.result = None

    def get_battle_status(self, battle_id):
        battle = self.battles.get(battle_id)
        if not battle:
            return None
        
        return {
            "status": battle.status,
            "result": battle.result
        }