import unittest
from pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pokemon1 = Pokemon(
            name="Pikachu",
            type1="electric",
            type2="",
            attack=55,
            against={"electric": 2, "water": 1, "fire": 1}
        )
        self.pokemon2 = Pokemon(
            name="Squirtle",
            type1="water",
            type2="",
            attack=48,
            against={"electric": 1, "water": 1, "fire": 1}
        )
        self.pokemon3 = Pokemon(
            name="Charizard",
            type1="fire",
            type2="flying",
            attack=84,
            against={"electric": 1, "water": 2, "fire": 1}
        )

    def test_calculate_damage_against_type1(self):
        # Pikachu against Squirtle (water type)
        damage = self.pokemon1.calculate_damage(self.pokemon2)
        self.assertEqual(damage, 2.5000000000000036)

    def test_calculate_damage_against_type2(self):
        # Charizard against Pikachu (electric type)
        damage = self.pokemon3.calculate_damage(self.pokemon1)
        self.assertEqual(damage, 17.0)

    def test_calculate_damage_against_both_types(self):
        # Pikachu against Charizard (fire and flying types)
        damage = self.pokemon1.calculate_damage(self.pokemon3)
        self.assertEqual(damage, 2.5000000000000036)

    def test_calculate_damage_no_effect(self):
        # Pikachu against itself (electric type)
        damage = self.pokemon1.calculate_damage(self.pokemon1)
        self.assertEqual(damage, -22.499999999999996)

if __name__ == '__main__':
    unittest.main()