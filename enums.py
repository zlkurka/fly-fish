from enum import Enum

class FishType(Enum):

    # Common
    trout = 'brown trout'
    rock_fish = 'rock fish'
    
    # Uncommon
    smallmouth = 'smallmouth bass'
    salmon = 'coho salmon'
    steel_head_trout = 'steel-head trout'

    # Rare
    steelhead = 'steelhead'
    muskellunge = 'muskellunge'
    silver_salmon = 'silver salmon'

    # Super rare
    gold_fish = 'gold fish'
        # Can be crafted into gold flakes
    
    # Dev
    common_fish = 'common fish'
    uncommon_fish = 'uncommon fish'
    rare_fish = 'rare fish'
    super_rare_fish = 'super rare fish'
    legendary_fish = 'legendary fish'

class Location(Enum):

    # In progress
    lake = 'the lake'
    river = 'the river'
    quarry = 'the quarry'

    # Not made yet
    pond = 'the pond'
    overpass = 'the overpass'

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

item_enums = [FishType, Location, Fly, Powerup]