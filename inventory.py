from flexible_menus import menu, counting_menu
from enums import FishType, Location, Fly, Powerup, item_enums
from fish_data import fish_pools, fish_values, powerup_casts, fly_odds, fly_times

class Inventory:
  
    # Setup inventory
    money: float = 0

    fish: dict = {}
    sus_fish: dict = {}

    flies: list[Fly] = [Fly.white]
    powerups: dict = {}
    locations: list[Location] = [Location.lake]

    recipes: dict = {}

    # Set defaults
    fly: Fly = flies[0]
    location: Location = locations[0]
    

    # Manage inv
    def check_inv(self):
        
        while True:
            print(f"\nYou have ${self.money}")
            match menu(['Fish','Flies','Locations','Powerups', 'Exit'],'What would you like to see?'):
                
                case 'Fish':
                    
                    if not self.fish and not self.sus_fish:
                        print("You don't have any fish!")
                    
                    else: 
                        print('You have:')
                        for itm in self.fish:
                            print(f"- {itm.value.capitalize()} ({self.fish[itm]}x)")
                        for itm in self.sus_fish:
                            print(f"- Suspicious {itm.value.capitalize()} ({self.sus_fish[itm]}x)")
                
                case 'Flies':
                    print('You have:')
                    for itm in self.flies:
                        print(f"- {itm.value.capitalize()} fly")

                case 'Locations':
                    print('You can go to:')
                    for itm in self.locations:
                        print(f"- {itm.value.capitalize()}")

                case 'Powerups':
                    
                    if not self.powerups:
                        print("You don't have any powerups!")

                    else: 
                        print('You have:')
                        for itm in self.powerups:
                            print(f"- {itm.value.capitalize()} ({self.powerups[itm]}x)")
                
                case 'Exit':
                    break
                
                case _:
                    print('Invalid option!')

    def add_items(self, item, *is_sus):
        
        if type(item) is dict and len(item) == 1:
            item_name = list(item)[0]
            item_count = item[item_name]
            item_type = type(list(item)[0])
        elif type(item) in item_enums:
            item_name = item
            item_count = 1
            item_type = type(item)
        else:
            print('Unacceptable item type!')
            item_name = item
            item_count = 1
            item_type = type(item)

        item_type = type(list(item)[0])

        # Fish
        if item_type == FishType and not is_sus:

            if item_name in self.fish:
                self.fish.update({item_name: item_count + self.fish[item_name]})
            else:
                self.fish.update({item_name: item_count})
        
        # Sus fish
        elif item_type == FishType and is_sus:

            if item_name in self.sus_fish:
                self.sus_fish.update({item_name: item_count + self.sus_fish[item_name]})
    
            else:
                self.sus_fish.update({item_name: item_count})
        
        # Powerup
        elif item_type == Powerup:
            
            if item_name in self.powerups:
                self.powerups.update({item_name: item_count + self.powerups[item_name]})
            else:
                self.powerups.update({item_name: item_count})
        
        # Fly
        elif item_type == Fly:

            if item_name not in self.flies:
                self.flies.append(item_name)
            else:
                print('You already have this fly!')
        
        # Unacceptable
        else:
            print('Unacceptable item type!')
    
    def remove_items(self, item, *is_sus):

        if type(item) is dict and len(item) == 1:
            item_name = list(item)[0]
            item_count = item[item_name]
            item_type = type(list(item)[0])
        elif type(item) in item_enums:
            item_name = item
            item_count = 1
            item_type = type(item)
        else:
            print('Unacceptable item type!')
            item_type = type(item)
        
        # Fish
        if item_type == FishType and not is_sus:

            if item_name not in self.fish:
                print("You don't have this fish!")
                return
            
            new_count = self.fish[item_name] - item_count
            if new_count < 0:
                print("You don't have that many!")
            elif new_count == 0:
                self.fish.pop(item_name)
            else:
                self.fish.update({item_name: new_count})
                
        # Sus fish
        elif item_type == FishType and is_sus:

            if item_name not in self.sus_fish:
                print("You don't have this fish!")
                return
            
            new_count = self.sus_fish[item_name] - item_count
            if new_count < 0:
                print("You don't have that many!")
            elif new_count == 0:
                self.sus_fish.pop(item_name)
            else:
                self.sus_fish.update({item_name: new_count})

        # Powerup    
        elif item_type == Powerup:

            if item_name not in self.powerups:
                print("You don't have this fish!")
                return
            
            new_count = self.powerups[item_name] - item_count
            if new_count < 0:
                print("You don't have that many!")
            elif new_count == 0:
                self.powerups.pop(item_name)
            else:
                self.powerups.update({item_name: new_count})
        
        # Fly
        elif item_type == Fly:

            if item_name in self.flies:
                self.flies.pop(item_name)
            else:
                print("You don't have this fly!")
        
        # Unacceptable
        else:
            print('Unacceptable item type!')

    def dev_mode(self):
        
        # Get all items in game

        for itm in Fly:
            if itm not in self.flies:
                self.flies.append(itm)

        for itm in Location:
            if itm not in self.locations:
                self.locations.append(itm)

        for itm in FishType:
            if itm not in self.fish and itm not in [FishType.common_fish,FishType.uncommon_fish,FishType.rare_fish,FishType.super_rare_fish,FishType.legendary_fish]:
                self.fish.update({itm:1})
        
        for itm in Powerup:
            if itm not in self.powerups:
                self.powerups.update({itm:99})

        self.money = 999
        self.fly = Fly.dev    


    # Change equipped
    def change_fly(self):
        print(f"You are currently using you {self.fly.value} fly.")
        self.fly = menu(self.flies,"What fly would you like to use?")
        print(f"You are now using your {self.fly.value} fly!")
    
    def travel(self):
        
        if len(self.locations) == 1:
            print(f'You can only access {self.locations[0]} right now')

        old_loc = self.location
        self.location = menu(self.locations, 'Where would you like to go?')
        
        if self.location == old_loc:
            print(f'You decide to stay at {self.location.value}.')
            return
        
        print(f'You travel from {old_loc.value} to {self.location.value}.')
    
    
    # Fishing
    def get_time(self):
        return fly_times[self.fly]
    
    def get_odds(self):
        return fly_odds[self.fly][0], fly_odds[self.fly][1], fly_odds[self.fly][2]
    
    def get_game(self):
        return fish_pools[self.location]

    def use_powerup(self, pups_in_use=dict):
        
        added_pups = {}

        if not self.powerups:
            print("You don't have any powerups!")
            return added_pups
        
        selection = counting_menu(self.powerups,'Which powerup would you like to use?')

        # All
        if selection == 'All':
            for pup in self.powerups:
                if pup not in pups_in_use:
                    self.remove_items(pup)
                    casts = powerup_casts[pup]
                    
                    added_pups.update({pup: casts})
                    print(f"{pup.value.capitalize()} is now active for {casts} casts.")
                else:
                    print(f"{pup.value.capitalize()} is already active.")
        
        # Powerup already in use
        elif selection in pups_in_use:
            print(f"{selection.value.capitalize()} is already active.")

        # Particular powerup
        elif selection:
            self.remove_items(selection)
            casts = powerup_casts[selection]

            added_pups.update({selection: casts})
            print(f"{selection.value.capitalize()} is now active for {casts} casts.")
        
        return added_pups
    

    # Shopping
    def change_money(self, change=int):
        self.money += change

    def get_value(self,fish=str):
        return fish_values[fish]
    
    def purchase(self, buy_item, item_count=int, item_price=float):
        while True:
            try: 
                buy_num = int(input(f'How many {buy_item.value} would you like to buy? (up to {item_count})\n'))
            
            except ValueError:
                print('Input only an integer (ex: 1)')
                continue

            if buy_num < 0:
                print('You cannot purchase negative fish!')
                continue

            if buy_num == 0:
                print('Sale cancelled')
                return item_count

            if buy_num <= item_count:

                sale_price = buy_num * item_price
                
                if sale_price > self.money:
                    print("You don't have that much money!")
                    continue

                self.change_money(-1 * sale_price)
                self.add_items({buy_item: buy_num})

                print(f'You bought {buy_num} {buy_item.value} for ${sale_price}.')

                return item_count - buy_num

            print("That's more than are in stock!")