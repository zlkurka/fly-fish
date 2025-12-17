from enum import Enum

class Fish(Enum):

    # Common
    trout = 'brown trout'
    common = 'common'
    
    # Uncommon
    smallmouth = 'smallmouth bass'
    salmon = 'coho salmon'
    uncommon = 'uncommon'

    # Rare
    steelhead = 'steelhead'
    muskellunge = 'muskellunge'
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