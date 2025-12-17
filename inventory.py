from string import ascii_uppercase
from collections import Counter
from flexible_menus import menu
from enums import Fish, Location, Fly, ItemType

class Inventory:
  
    # Setup inventory
    money: float = 0
    fish: dict
    powerups: dict
    flies: list[str] = [Fly.white]
    locations: list[str] = [Location.dells]
    
    # Set defaults
    fly: str = Fly.white
    location: str = Location.dells
  

  # Fish
    def add_items(self, items, item_type=str):
        
        match item_type:

            case 'fish':

                if type(items) is list:
                    fish_dict = {}
                    for fsh in items:
                        fish_dict.update({items:1})
                if type(items) is str:
                    items = {items:1}

                new_fish = list(items)[0]

                if new_fish in self.fish:

                    self.fish.update({
                        new_fish:
                        items.get(new_fish) + self.fish.get(new_fish)})
                
                else:
                    self.fish.update(items)
            
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
                print(f'You do not have that many {fish_name}')
          
        else:
          print('You do not have this fish!')

    def see_fish(self, *text):

        if not self.fish:
            try: 
                print(text[1])
            except IndexError:
                print("You don't have any fish!")

        else: 
            fish_counted = Counter(self.fish)

            print(text[0])
            for fsh in fish_counted:
                print(f'- {fish_counted[fsh]} {fsh}')
    

    # Flies
    def add_fly(self, new_fly=str):
        if new_fly not in self.flies:
            self.flies.append(new_fly)
        else:
            print('You already have this fly!')

    def change_fly(self):
        self.fly = menu(self.flies,"What fly would you like to use?")
    
    
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
        return fly_times.get(self.fly, 0)
    
    def get_odds(self):
      
        fly_odds = {
            
            # [0]% chance to catch a common fish, [1]-[0]% chance for uncommon, [2]-[1]-[0]% for rare

            'white': [30,40,45],
            'red': [10,20,40],
            'gold': [50,70,80],

            'dev': [33,66,100],
            'dev_shit': [0,1,2],
        }
        return fly_odds.get(self.fly, 0)
    
    def get_game(self):
      
        fish_pools = {
            Location.dells: [Fish.trout,Fish.smallmouth,Fish.muskellunge],
            Location.chicago: [Fish.trout,Fish.salmon,Fish.steelhead],
            Location.dev: [Fish.common,Fish.uncommon,Fish.rare]
        }
        
        return fish_pools.get(self.location)
    

    # Shopping
    def change_money(self, change=int):
        self.money += change

    def get_value(self,fish=str):
      
        fish_values = {
            
            # Common fish
            Fish.common: 5,
            Fish.trout: 5,
            
            # Uncommon fish
            Fish.uncommon: 7,
            Fish.smallmouth: 7,
            Fish.salmon: 8,

            # Rare fish
            Fish.rare: 15,
            Fish.muskellunge: 13, 
            Fish.steelhead: 16,
            
        }

        return fish_values.get(fish, 0)
    
    def purchase(self, buy_item=str, item_count=int, item_price=float):
        while True:
            try: 
                
                buy_num = int(input(f'How many {buy_item} would you like to buy? (up to {item_count})\n'))
                
                if buy_num == 0:
                    print('Sale cancelled')
                    break

                elif buy_num <= item_count:

                    sale_price = buy_num * item_price
                    if sale_price > self.money:
                        print("You don't have that much money!")

                    self.change_money(-1 * sale_price)
                    self.remove_fish({buy_item:buy_num})

                    print(f'You bought {buy_num} {buy_item} for ${sale_price}.')

                    return (item_count - buy_num)

                else:
                    print("That's more than are in stock!")
                    
            except ValueError:
                print('Input only an integer (ex: 1)')

    # Other
    def dev_mode(self):
        
        # Get all items in game

        for item in Fly:
            if item not in self.flies:
                self.flies.append(item)

        for item in Location:
            if item not in self.locations:
                self.locations.append(item)

        for item in Fish:
            if item not in self.fish:
                self.fish.append(item)

        self.money = 999

        self.fly = Fly.dev
        self.location = Location.dev


def testing():
  
    inventory = Inventory()

    for num in range(5):
        inventory.add_item({Fish.trout:1},ItemType.fish)
        print(f"You have {inventory.fish[Fly.trout]} brown trout")
        input()
    inventory.see_fish('You have: ')

    inventory.add_fly(Fly.red)
    inventory.change_fly(Fly.red)
    print(f"You are using your {inventory.fly} fly")