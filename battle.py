import uuid
from pokemon import Pokemon

class Battle:
    def __init__(self, pokemon_a: Pokemon, pokemon_b: Pokemon):
        self.pokemon_a = pokemon_a
        self.pokemon_b = pokemon_b
        self.battle_id = uuid.uuid4()
        self.result = None
        self.status = "BATTLE_INPROGRESS"

    def start(self):
        damage_a_to_b = self.pokemon_a.calculate_damage(self.pokemon_b)
        damage_b_to_a = self.pokemon_b.calculate_damage(self.pokemon_a)
        
        if damage_a_to_b > damage_b_to_a:
            winner = self.pokemon_a
            margin = damage_a_to_b - damage_b_to_a
        elif damage_b_to_a > damage_a_to_b:
            winner = self.pokemon_b
            margin = damage_b_to_a - damage_a_to_b
        else:
            winner = None
            margin = 0
        
        self.result = {
            "winnerName": winner.name if winner else "Draw",
            "wonByMargin": margin
        }
        self.status = "BATTLE_COMPLETED" if winner else "BATTLE_DRAW"