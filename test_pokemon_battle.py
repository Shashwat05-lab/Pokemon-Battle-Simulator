import unittest
from unittest.mock import MagicMock, patch
from pokemon_battle import PokemonBattleAPI
from pokemon import Pokemon
from battle import Battle

class TestPokemonBattleAPI(unittest.TestCase):

    def setUp(self):
        self.api = PokemonBattleAPI()

    @patch('pokemon_battle.Pokemon')
    def test_load_pokemons(self, MockPokemon):
        # Mock the Pokemon constructor to avoid actual instantiation
        mock_pokemon_instance = MagicMock(spec=Pokemon)
        MockPokemon.return_value = mock_pokemon_instance

        # Sample CSV content
        csv_content = """name,type1,type2,attack,against_normal,against_fire
                        Bulbasaur,grass,poison,49,1.0,0.5
                        Charmander,fire,,52,1.0,0.5"""

        # Writing the content to a temporary CSV file
        with open('test_pokemon.csv', 'w') as f:
            f.write(csv_content)

        # Load the CSV into the API
        self.api.load_pokemons('test_pokemon.csv')

        self.assertEqual(len(self.api.pokemons), 2)

    def test_get_pokemons(self):
        self.api.pokemons = {
            'bulbasaur': MagicMock(spec=Pokemon),
            'charmander': MagicMock(spec=Pokemon),
            'squirtle': MagicMock(spec=Pokemon)
        }
        
        result = self.api.get_pokemons(page=1, per_page=2)
        self.assertEqual(result, ['bulbasaur', 'charmander'])

        result = self.api.get_pokemons(page=2, per_page=2)
        self.assertEqual(result, ['squirtle'])

    @patch('pokemon_battle.ThreadPoolExecutor')
    @patch('pokemon_battle.Battle')
    def test_start_battle(self, MockBattle, MockExecutor):
        self.api.pokemons = {
            'bulbasaur': MagicMock(spec=Pokemon),
            'charmander': MagicMock(spec=Pokemon)
        }

        mock_battle_instance = MagicMock(spec=Battle)
        MockBattle.return_value = mock_battle_instance
        mock_battle_instance.battle_id = 'mock_id'

        # Mock the executor instance and its submit method
        mock_executor_instance = MagicMock()
        MockExecutor.return_value = mock_executor_instance

        # Start a battle
        battle_id = self.api.start_battle('Bulbasaur', 'Charmander')

        self.assertEqual(battle_id, 'mock_id')

    @patch('pokemon_battle.Battle')
    def test_get_battle_status(self, MockBattle):
        mock_battle_instance = MagicMock(spec=Battle)
        mock_battle_instance.status = 'BATTLE_INPROGRESS'
        mock_battle_instance.result = None
        self.api.battles['mock_id'] = mock_battle_instance

        status = self.api.get_battle_status('mock_id')

        self.assertEqual(status['status'], 'BATTLE_INPROGRESS')
        self.assertIsNone(status['result'])

    def test_get_battle_status_invalid_id(self):
        status = self.api.get_battle_status('invalid_id')
        self.assertIsNone(status)

if __name__ == "__main__":
    unittest.main()