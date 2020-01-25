import random


class Spell:
    def __init__(self, name, cost, damage, spell_type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = spell_type

    def generate_spell_damage(self):
        low = self.damage - 15
        high = self.damage + 15
        return random.randrange(low, high)
