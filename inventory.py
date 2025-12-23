from string import ascii_uppercase

from flexible_menus import menu
from enums import FishType, Location, Fly, ItemType
from fish_data import fish_pools, fish_values

class Inventory:
  
    # Setup inventory
    money: float = 0

    fish: dict = {}
    sus_fish: dict = {}

    flies: list[Fly] = [Fly.white]
    powerups: dict = {}
    locations: list[Location] = [Location.lake]
    
    # Set defaults
    fly: Fly = flies[0]
    location: Location = locations[0]
  

    # Fish
    def add_items(self, items, item_type=ItemType):
        
        if type(items) is list:
            
            items_list = items
            items = {}

            for itm in items_list:
                if itm in items:
                    items.update({itm:items[itm]+1})
                else:
                    items.update({itm:1})

        if type(items) is str:
            items = {items:1}

        match item_type:

            case ItemType.fish:

                for fsh in items:

                    if fsh in self.fish:
                        self.fish.update({fsh:items[fsh] + self.fish[fsh]})
            
                    else:
                        self.fish.update({fsh:items[fsh]})
            
            case ItemType.sus_fish:

                for fsh in items:

                    if fsh in self.sus_fish:
                        self.sus_fish.update({fsh:items[fsh] + self.sus_fish[fsh]})
            
                    else:
                        self.sus_fish.update({fsh:items[fsh]})
            
            case _:
                print('Unacceptable item type!')
    
    def remove_fish(self, fish=dict):

        fish_name = list(fish)[0]

        if fish_name in self.fish:
          
            if fish.get(fish_name) <= self.fish.get(fish_name):
                self.fish.update({
                    fish_name:
                    fish.get(fish_name) - self.fish.get(fish_name)})
                if self.fish.get(fish_name) == 0:
                    self.fish.pop(fish_name)
            
            else:
                print(f'You do not have that many {fish_name.value}')
          
        else:
          print('You do not have this fish!')

    def see_fish(self, *text):

        if not self.fish and not self.sus_fish:
            try: 
                print(text[1])
            except IndexError:
                print("You don't have any fish!")

        else: 
            print(text[0])
            for fsh in self.fish:
                print(f'- {self.fish[fsh]} {fsh.value}')
            for fsh in self.sus_fish:
                print(f'- {self.sus_fish[fsh]} suspicious {fsh.value}')
    

    # Flies
    def add_fly(self, new_fly=str):
        if new_fly not in self.flies:
            self.flies.append(new_fly)
        else:
            print('You already have this fly!')

    def change_fly(self):
        print(f"You are currently using you {self.fly.value} fly.")
        self.fly = menu(self.flies,"What fly would you like to use?")
        print(f"You are now using your {self.fly.value} fly!")
    
    
    # Fishing
    def get_time(self):
      
        fly_times = {
            
              # [0] = base time, +/- a randint beteen -1*[1] and [1]

              Fly.white: [10,4],
              Fly.red: [15,5],
              Fly.gold: [7,3],

              Fly.dev: [2,0],
              Fly.dev_shit: [2,0],
        }
        return fly_times[self.fly]\
    
    def get_odds(self):
      
        fly_odds = {
            
            # [0]% chance to catch a common fish, [1]-[0]% chance for uncommon, [2]-[1]-[0]% for rare

            Fly.white: [30,40,45],
            Fly.red: [15,35,60],
            Fly.gold: [50,70,80],

            Fly.dev: [33,66,99],
            Fly.dev_shit: [0,1,2],
        }
        return fly_odds[self.fly]
    
    def get_game(self):
        return fish_pools[self.location]

    # Shopping
    def change_money(self, change=int):
        self.money += change

    def get_value(self,fish=str):
        return fish_values.get(fish, 0)
    
    def purchase(self, buy_item, item_count=int, item_price=float, item_type=ItemType):
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
                return 0

            if buy_num <= item_count:

                sale_price = buy_num * item_price
                
                if sale_price > self.money:
                    print("You don't have that much money!")
                    continue

                self.change_money(-1 * sale_price)
                self.add_items({buy_item:buy_num}, item_type)

                print(f'You bought {buy_num} {buy_item.value} for ${sale_price}.')

                return (item_count - buy_num)

            print("That's more than are in stock!")

    # Other
    def dev_mode(self):
        
        # Get all items in game

        for itm in Fly:
            if itm not in self.flies:
                self.flies.append(itm)

        for itm in Location:
            if itm not in self.locations:
                self.locations.append(itm)

        for itm in FishType:
            if itm not in self.fish:
                self.fish.update({itm:1})

        self.money = 999
        self.fly = Fly.dev


def testing():
  
    inventory = Inventory()

    for num in range(5):
        inventory.add_item({FishType.trout:1},ItemType.fish)
        print(f"You have {inventory.fish[Fly.trout]} brown trout")
        input()
    inventory.see_fish('You have: ')

    inventory.add_fly(Fly.red)
    inventory.change_fly(Fly.red)
    print(f"You are using your {inventory.fly} fly")