from arena import Arena
from character import Mage, Rogue, Tank, Warrior
from equipment import Armor, Weapon
from item import Bomb, Elixir, Potion

# Fighters
kaelen = Warrior("Kaelen", 120, 12)
elara = Mage("Elara", 50, 6) 
vesper = Rogue("Vesper", 75, 10)
tank = Tank("Gareth", 200, 5)

# Weapons / Armor
great_sword = Weapon("Greatsword", 8)
arcane_staff = Weapon("Arcane Staff", 2)
poison_dagger = Weapon("Poisoned Dagger", 4)
war_hammer = Weapon("Warhammer", 5)
knight_plate = Armor("Knight's Plate", 6)
iron_plate = Armor("Iron Plate", 4)
silk_robe = Armor("Silk Robe", 2)
shadow_cloak = Armor("Shadow Cloak", 3)
iron_bulwark = Armor("Iron Bulwark", 8)

# Items
potion = Potion("Health Potion", 20)
bomb = Bomb("Fire Bomb", 20)
elixir = Elixir("Elixir")

# Equip gear
kaelen.equip_weapon(great_sword)
kaelen.equip_armor(knight_plate)
kaelen.add_item(potion)

elara.equip_weapon(arcane_staff)
elara.equip_armor(silk_robe)
elara.add_item(potion)
elara.add_item(bomb)

vesper.equip_weapon(poison_dagger)
vesper.equip_armor(shadow_cloak)
vesper.add_item(potion)
vesper.add_item(elixir)

tank.equip_weapon(war_hammer)
tank.equip_armor(iron_bulwark)
tank.add_item(bomb)

fighters = [kaelen, elara, vesper, tank]

print("\nWelcome to the RPG Arena!")
print("\nChoose your fighters: ")

for i, fighter in enumerate(fighters, start=1):
    print(f"{i}. {fighter.name} ({fighter.__class__.__name__})")

# Selecting chracters
choice1 = int(input("Select Fighter 1 (number): "))
fighter1 = fighters[choice1 - 1] 

choice2 = int(input("Select Fighter 2 (number): "))
fighter2 = fighters[choice2 - 1] 

# Start game
my_arena = Arena(fighter1, fighter2)
my_arena.fight()