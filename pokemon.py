from typing import Dict

class Pokemon:
    def __init__(self, name: str, type1: str, type2: str, attack: int, against: Dict[str, float]):
        self.name = name.lower()
        self.type1 = type1.lower()
        self.type2 = type2.lower()
        self.attack = attack
        self.against = against

    def calculate_damage(self, opponent) -> float:
        damage = (self.attack / 200) * 100
        if opponent.type1 in self.against:
            damage -= (self.against[opponent.type1] / 4) * 100
        if opponent.type2 in self.against:
            damage -= (self.against[opponent.type2] / 4) * 100
        return damage
