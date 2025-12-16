from string import ascii_uppercase
from collections import Counter
from flexible_menu import menu

class Inventory:
  
    # Setup inventory
    money: float = 0
    fish: dict = {}
    powerups: dict = {}
    flies: list[str] = ['white']
    locations: list[str] = ['The Dells']
    
    # Set defaults
    fly: str = 'white'
    location: str = 'The Dells'
  

  # Fish
    def add_fish(self, fish):
        # fish is a dict, e.g., {'brown trout': 1}
        
        if type(fish) is list:
            fish_dict = {}
            for fsh in fish:
                fish_dict.update({fish:1})
        if type(fish) is str:
            fish = {fish:1}

        new_fish = list(fish)[0]

        if new_fish in self.fish:

            self.fish.update({
                new_fish:
                fish.get(new_fish) + self.fish.get(new_fish)})
          
        else:
            self.fish.update(fish)
    
    def remove_fish(self, fish):

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
    def add_fly(self, new_fly):
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

              'white': [10,4],
              'red': [15,5],
              'gold': [7,3],

              'dev': [2,0],
              'dev_shit': [2,0],
        }
        return fly_times.get(self.fly, 0)
    
    def get_odds(self):
      
        fly_odds = {
            
            # [0]% chance to catch a common fish, [1]% chance for uncommon, [2]% for rare

            'white': [20,30,35],
            'red': [10,20,40],
            'gold': [50,70,80],

            'dev': [33,66,100],
            'dev_shit': [0,1,2],
        }
        return fly_odds.get(self.fly, 0)
    
    def get_game(self):
      
        fish_pools = {
            'the dells': ['brown trout','smallmouth bass','muskellunge'],
            'chicago': ['brown trout','coho salmon','steelhead'],
            'dev': ['common','uncommon','rare']
        }
        
        return fish_pools.get(self.location, 0)
    

    # Shopping
    def change_money(self, change):
        self.money += change

    def get_value(self,fish):
      
        fish_values = {
            
            # Common fish
            'common': 5,
            'brown trout': 5,
            
            # Uncommon fish
            'uncommon': 7,
            'smallmouth bass': 7,
            'coho salmon': 8,

            # Rare fish
            'rare': 15,
            'muskellunge': 13, 
            'steelhead': 16,
            
        }

        return fish_values.get(fish, 0)
    
    def dev_mode(self):
        self.flies = ['white','red','gold','dev','dev_shit']
        self.locations = ['the dells','chicago','dev']
        self.money = 999

        self.fly = 'dev'
        self.location = 'dev'
        
        current_locat = self.location
        for locat in self.locations:
            self.location = locat
            for fsh in self.get_game():
                self.add_fish(fsh)
        self.location = current_locat


def testing():
  
    inventory = Inventory()

    for num in range(5):
        inventory.add_fish({'brown trout':1})
        print(f'You have {inventory.fish['brown trout']} brown trout')
        input()
    inventory.see_fish('You have: ')

    inventory.add_fly('red')
    inventory.change_fly()
    print(f'You are using your {inventory.fly} fly')