class Arena:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.current_turn = fighter1
        self.next_turn = fighter2

    def swap_turns(self):
        self.current_turn, self.next_turn = (self.next_turn, self.current_turn)

    def fight(self):
        while self.fighter1.is_alive() and self.fighter2.is_alive():
            print("\n" + "="*30)
            print(self.fighter1)
            print(self.fighter2)
            print("="*30)

            print(f"\n{self.current_turn.name}'s turn!")
            print("\n1. Attack")
            print("2. Use Special Ability")
            print("3. Use Item")

            user_choice = input("\nChoose action: ")
            if user_choice == "1":
                damage = self.current_turn.attack(self.next_turn)
                print(f"\n⚔️  {self.current_turn.name} attacks!")
                if damage == 0:
                    print(f"💨  {self.next_turn.name} dodged the attack!")
                    print(f"❤️  {self.next_turn.name} is still at {self.next_turn.hp} HP.")
                else:
                    print(f"💥  It dealt {damage} damage!")
                    print(f"❤️  {self.next_turn.name} is now at {self.next_turn.hp} HP.")

            elif user_choice == "2":
                if hasattr(self.current_turn, "cast_spell"):
                    result = self.current_turn.cast_spell(self.next_turn)
                    if isinstance(result, int):
                        print(f"{self.current_turn.name} blasted {self.next_turn.name} for {result} fire damage!")
                    else:
                        print(result)
                elif hasattr(self.current_turn, "vanish"):
                    self.current_turn.vanish()
                    print(f"{self.current_turn.name} vanished! 💨")
                elif hasattr(self.current_turn, "cast_heal"):
                    self.current_turn.cast_heal()
                    print(f"{self.current_turn.name} casted a healing spell! ")
                    print(f"{self.current_turn.name} ")
                elif hasattr(self.current_turn, "shield"):
                    self.current_turn.shield()
                    print(f"{self.current_turn.name} raised their shield!")
                else:
                    print("No active special ability.")

            elif user_choice == "3":
                if len(self.current_turn.inventory) == 0:
                    print("No item to use!")
                else:
                    for i, item in enumerate(self.current_turn.inventory):
                        print(f"{i + 1}. {item}")
                    choice = int(input("Choose your item: "))
                    item_index = choice - 1
                    item = self.current_turn.inventory[item_index]
                    item.use(self.current_turn)
                    self.current_turn.inventory.pop(item_index)

            self.swap_turns()

        if self.fighter1.is_alive():
            print("\n" + "="*30)
            print(f"🏆 {self.fighter1.name} WINS THE ARENA! 🏆")
            print("="*30)
        else:
            print("\n" + "="*30)
            print(f"🏆 {self.fighter2.name} WINS THE ARENA! 🏆")
            print("="*30)