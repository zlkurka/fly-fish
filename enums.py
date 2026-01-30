from enum import Enum

class FishType(Enum):

    # Common
    trout = 'brown trout'
    rock_fish = 'rock fish'
    hell_crab_b = 'blue hell-crab'
    
    # Uncommon
    smallmouth = 'smallmouth bass'
    salmon = 'coho salmon'
    steel_head_trout = 'steel-head trout'
    hell_crab_p = 'periwinkle hell-crab'

    # Rare
    steelhead = 'steelhead'
    muskellunge = 'muskellunge'
    silver_salmon = 'silver salmon'
    satan_eel = 'satan eel'

    # Super rare
    gold_fish = 'gold fish'
    angel_fish = 'angel fish'
    
    # Legendary
    diamond_tetra = 'diamond tetra'
    biblical_angel = 'biblically accurate angelfish'

    # Dev
    common = 'common fish'
    uncommon = 'uncommon fish'
    rare = 'rare fish'
    super_rare = 'super rare fish'
    legendary = 'legendary fish'

class Location(Enum):
    
    quarry = 'the quarry'
    hell = 'Hell'

    # In progress
    lake = 'the lake'
    river = 'the river'

    # Not made yet
    pond = 'the pond'
    overpass = 'the overpass'

    # dev
    blank = 'BLANK'

class Fly(Enum):
    
    # Original
    white = 'white'
    red = 'red'
    gold = 'gold'

    # New
    magnet = 'magnet'
    soul = 'soul fragment'
    double = 'double'

    # Dev
    dev = 'DEV'
    dev_shit = 'SHIT'

class Powerup(Enum):

    sake = 'sake'
    coffee = 'coffee grounds'
    gold_flakes = 'gold flakes'

class Rarity(Enum):
    
    # Rarities
    common = 'common'
    uncommon = 'uncommon'
    rare = 'rare'
    super_rare = 'super rare'
    legendary = 'legendary'

class Merchant(Enum):

    fishmonger = 'Fishmonger'
    drink_lady = 'Drink Lady'

class Material(Enum):

    hook = 'hook'

item_enums = [FishType, Location, Fly, Powerup]