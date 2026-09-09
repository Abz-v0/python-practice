class Potion:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def use(self, target):
        target.heal(self.value)
    def __str__(self):
        return f"{self.name} (+{self.value} HP)"

class Bomb:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def use(self, target):
        target.take_damage(self.value)
    def __str__(self):
        return f"{self.name} ({self.value} damage)"
    
class Elixir:
    def __init__(self, name):
        self.name = name
    def use(self, target):
        if hasattr(target, "heal_used"):
            target.heal_used = False
        if hasattr(target, "spell_cooldown"):
            target.spell_cooldown = 0
        if hasattr(target, "vanished"):
            target.vanished = True
        if hasattr(target, "shield_is_up"):
            target.shield_is_up = True
        print(f"Used {self.name} on {target.name}! Special reset.")
    def __str__(self):
        return f"{self.name} (Resets special ability)"