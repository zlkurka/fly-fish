from enum import Enum

class FishType(Enum):

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

class Rarity(Enum):
    
    # Rarities
    common = 'common'
    uncommon = 'uncommon'
    rare = 'rare'

def testing():
    print(FishType.trout)
    print(FishType.trout.value.capitalize())
    print(FishType.trout.name.upper())

    print(type(FishType.trout))
    print(type(FishType.trout.name))
    print(type(FishType.trout.value))