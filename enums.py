from enum import Enum

class FishType(Enum):

    # Common
    trout = 'brown trout'
    
    # Uncommon
    smallmouth = 'smallmouth bass'
    salmon = 'coho salmon'

    # Rare
    steelhead = 'steelhead'
    muskellunge = 'muskellunge'

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
    sus_fish = 'suspicious fish'

class Rarity(Enum):
    
    # Rarities
    common = 'common'
    uncommon = 'uncommon'
    rare = 'rare'

class Merchant(Enum):

    fishmonger = 'Fishmonger'
    drink_lady = 'Drink Lady'

def testing():
    print(FishType.trout)
    print(FishType.trout.value.capitalize())
    print(FishType.trout.name.upper())

    print(type(FishType.trout))
    print(type(FishType.trout.name))
    print(type(FishType.trout.value))