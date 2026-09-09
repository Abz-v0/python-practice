class Weapon:
    def __init__(self, name, damage_bonus, effect=None):
        self.name = name
        self.damage_bonus = damage_bonus
        self.effect = effect

    def __str__(self):
        return f"{self.name} (+{self.damage_bonus} damage)"

class Armor:
    def __init__(self, name, defense_value):
        self.name = name
        self.defense_value = defense_value

    def __str__(self):
        return f"{self.name} (-{self.defense_value} damage taken)"