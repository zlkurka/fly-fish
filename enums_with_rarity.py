from enum import Enum

class Fish(Enum):

    def __init__(self):
        if self in [self.trout,self.common_fish]:
            rarity = self.common
        elif self in [self.smallmouth,self.salmon,self.uncommon_fish]:
            rarity = self.uncommon
        elif self in [self.steelhead,self.muskellunge,self.rare_fish]:
            rarity = self.rare
        else:
            print('Fish rarity not found!')
            rarity = None

    # Common
    trout = 'brown trout'
    common_fish = 'common'
    
    # Uncommon
    smallmouth = 'smallmouth bass'
    salmon = 'coho salmon'
    uncommon_fish = 'uncommon'

    # Rare
    steelhead = 'steelhead'
    muskellunge = 'muskellunge'
    rare_fish = 'rare'

    # Rarities
    common = 'common'
    uncommon = 'uncommon'
    rare = 'rare'

class Location(Enum):

    # Old locations
    dells = 'The Dells'
    chicago = 'Chicago'

    # New locations
    lake = 'the lake'
    river = 'the river'
    pond = 'the pond'
    overpass = 'the overpass'

    # Dev
    dev = 'DEV'

class Fly(Enum):
    
    # Original
    white = 'white'
    red = 'red'
    gold = 'gold'

    # New
    magnet = 'magnet'

    # Dev
    dev = 'DEV'
    dev_shit = 'SHIT'

class Powerup(Enum):

    sake = 'sake'
    coffee = 'coffee grounds'
    gold_flakes = 'gold flakes'

class ItemType(Enum):

    fish = 'fish'


def testing():
    print(Fish.trout)
    print(Fish.trout.value.capitalize())
    print(Fish.trout.name.upper())

    print(type(Fish.trout))
    print(type(Fish.trout.name))
    print(type(Fish.trout.value))