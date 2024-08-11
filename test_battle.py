import unittest
from unittest.mock import MagicMock
from battle import Battle
from pokemon import Pokemon
import uuid

class TestBattle(unittest.TestCase):

    def setUp(self):
        # Create mock Pokemon instances
        self.pokemon_a = MagicMock(spec=Pokemon)
        self.pokemon_b = MagicMock(spec=Pokemon)
        self.pokemon_a.name = "Pikachu"
        self.pokemon_b.name = "Charmander"
    
    def test_battle_winner_a(self):
        # Set up mock damage calculations
        self.pokemon_a.calculate_damage.return_value = 50
        self.pokemon_b.calculate_damage.return_value = 30

        battle = Battle(self.pokemon_a, self.pokemon_b)
        battle.start()

        self.assertEqual(battle.result["winnerName"], "Pikachu")
        self.assertEqual(battle.result["wonByMargin"], 20)
        self.assertEqual(battle.status, "BATTLE_COMPLETED")
    
    def test_battle_winner_b(self):
        # Set up mock damage calculations
        self.pokemon_a.calculate_damage.return_value = 20
        self.pokemon_b.calculate_damage.return_value = 40

        battle = Battle(self.pokemon_a, self.pokemon_b)
        battle.start()

        self.assertEqual(battle.result["winnerName"], "Charmander")
        self.assertEqual(battle.result["wonByMargin"], 20)
        self.assertEqual(battle.status, "BATTLE_COMPLETED")
    
    def test_battle_draw(self):
        # Set up mock damage calculations
        self.pokemon_a.calculate_damage.return_value = 30
        self.pokemon_b.calculate_damage.return_value = 30

        battle = Battle(self.pokemon_a, self.pokemon_b)
        battle.start()

        self.assertEqual(battle.result["winnerName"], "Draw")
        self.assertEqual(battle.result["wonByMargin"], 0)
        self.assertEqual(battle.status, "BATTLE_DRAW")

    def test_battle_id_generation(self):
        battle = Battle(self.pokemon_a, self.pokemon_b)
        self.assertIsNotNone(battle.battle_id)
        self.assertIsInstance(battle.battle_id, uuid.UUID)

if __name__ == "__main__":
    unittest.main()