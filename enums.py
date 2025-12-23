from enum import Enum

class FishType(Enum):

    # Common
    trout = 'brown trout'
    
    # Uncommon
    smallmouth = 'smallmouth bass'
    salmon = 'coho salmon'
    steel_head = 'steel head'

    # Rare
    steelhead = 'steelhead'
    muskellunge = 'muskellunge'
    gold_fish = 'gold fish'
        # Can be crafted into gold flakes
    
    # Dev
    common_fish = 'common fish'
    uncommon_fish = 'uncommon fish'
    rare_fish = 'rare fish'
    super_rare_fish = 'super rare fish'

class Location(Enum):

    lake = 'the lake'
    river = 'the river'
    pond = 'the pond'
    overpass = 'the overpass'
    quarry = 'the quarry'

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
    super_rare = 'super rare'

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