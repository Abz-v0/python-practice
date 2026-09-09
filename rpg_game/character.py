import random

from equipment import Armor, Weapon


class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.weapon = None
        self.armor = None
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def equip_armor(self, armor: Armor):
        self.armor = armor

    def attack(self, target):
        damage = self.attack_power
        if self.weapon is not None:
            damage = damage + self.weapon.damage_bonus
        actual_damage = target.take_damage(damage)
        return actual_damage

    def take_damage(self, amount):
        if self.armor is not None:
            amount = amount - self.armor.defense_value
            amount = max(0, amount)
        self.hp = max(self.hp - amount, 0)
        return amount

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        stats = f"{self.name} (HP: {self.hp}/{self.max_hp})"

        stats += f" | ATK: {self.attack_power}"
        if self.weapon is not None:
            stats += f" (+{self.weapon.damage_bonus})"
            
        if self.armor is not None:
            stats += f" | DEF: {self.armor.defense_value}"
            
        stats += f" | Items: {len(self.inventory)}"
    
        return stats

class Warrior(Character):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.attack_count =  0
    def attack(self, target):
        damage = self.attack_power
        self.attack_count += 1
        if self.attack_count == 3:
            damage = self.attack_power + 10
            self.attack_count = 0
        else:
            damage = self.attack_power
        if self.weapon is not None:
            damage += self.weapon.damage_bonus
        
        actual_damage = target.take_damage(damage)
        return actual_damage


# Mage: can cast_spell(target) — fireball ignores armor; can heal() once per fight
class Mage(Character):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.heal_used = False
        self.spell_cooldown = 0
    def attack(self, target):
        damage = self.attack_power 
        if self.spell_cooldown > 0:
            self.spell_cooldown -= 1
        if self.weapon is not None:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)
        return damage
    def cast_spell(self, target):
        if self.spell_cooldown > 0:
            return "Spell is on cooldown!"
        spell_damage = 25
        target.hp = max(target.hp - spell_damage, 0)
        self.spell_cooldown = 3 
        return spell_damage
    def cast_heal(self):
        if self.heal_used:
            return "Heal already used."
        self.hp = min(self.hp + 20, self.max_hp)
        self.heal_used = True
        return f"Healed: HP: {self.hp}"

# Rogue: 25% chance for triple damage; can vanish() to dodge next attack
class Rogue(Character):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.vanished = False
    def vanish(self):
        self.vanished = True
    def take_damage(self, amount):
        if self.vanished == True:
            amount = 0
            self.vanished = False
        super().take_damage(amount)
        return amount
    def attack(self, target):
        damage = self.attack_power
        if random.random() < 0.25:
            damage = damage * 3
        if self.weapon is not None:
            damage += self.weapon.damage_bonus
        target.take_damage(damage)
        return damage

# Tank: high HP; can shield() to halve damage for one turn
class Tank(Character):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.shield_is_up = False
    def shield(self):
        self.shield_is_up = True
    def take_damage(self, amount):
        if self.shield_is_up == True:
            amount = amount // 2
            self.shield_is_up = False
        super().take_damage(amount)
        return amount