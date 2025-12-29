from enums import FishType, Location, Rarity, Powerup, Fly, Merchant

# Fish

fish_pools = {

    Location.lake: {
        Rarity.common: [FishType.trout],
        Rarity.uncommon: [FishType.smallmouth],
        Rarity.rare: [FishType.muskellunge],
        Rarity.super_rare: [FishType.super_rare_fish],
        Rarity.legendary: [FishType.legendary_fish],
    },
    Location.river: {
        Rarity.common: [FishType.trout],
        Rarity.uncommon: [FishType.salmon],
        Rarity.rare: [FishType.steelhead],
        Rarity.super_rare: [FishType.super_rare_fish],
        Rarity.legendary: [FishType.legendary_fish],
    },
    Location.quarry: {
        Rarity.common: [FishType.rock_fish],
        Rarity.uncommon: [FishType.steel_head_trout],
        Rarity.rare: [FishType.silver_salmon],
        Rarity.super_rare: [FishType.gold_fish],
        Rarity.legendary: [FishType.diamond_tetra],
    },
}

def set_rarities():
    fish_rarities = {
        Rarity.common: [],
        Rarity.uncommon: [],
        Rarity.rare: [],
        Rarity.super_rare: [],
        Rarity.legendary: [],
    }
    
    for loc in fish_pools:
        for rar in Rarity:
            
            if fish_rarities[rar]:
                fish_rarities.update({rar: list(set(fish_rarities[rar] + fish_pools[loc][rar]))})
            else:
                fish_rarities.update({rar: fish_pools[loc][rar]})
    
    return fish_rarities

fish_rarities = set_rarities()

fish_materials = {
            
    # Common fish
    FishType.trout: [],
    FishType.rock_fish: [],
    
    # Uncommon fish
    FishType.smallmouth: [],
    FishType.salmon: [],
    FishType.steel_head_trout: [],

    # Rare fish
    FishType.muskellunge: [], 
    FishType.steelhead: [],

    # Super rare fish
    FishType.gold_fish: [Powerup.gold_flakes],
}


# Flies

fly_odds = {
            
    # [0]% chance to catch a common fish, [1]-[0]% chance for uncommon, [2]-[1]-[0]% for rare

    Fly.white: [30,40,45],
    Fly.red: [15,35,60],
    Fly.gold: [50,70,80],

    Fly.dev: [33,66,99],
    Fly.dev_shit: [0,1,2],
}

fly_times = {
            
    # [0] = base time, +/- a randint between 0 and [1]

    Fly.white: [10,4],
    Fly.red: [15,5],
    Fly.gold: [7,3],

    Fly.dev: [2,0],
    Fly.dev_shit: [2,0],
}


# Shopping

fish_values = {
            
    # Common fish
    FishType.trout: 5,
    FishType.rock_fish: 3,
    
    # Uncommon fish
    FishType.smallmouth: 7,
    FishType.salmon: 8,
    FishType.steel_head_trout: 14,

    # Rare fish
    FishType.muskellunge: 13, 
    FishType.steelhead: 16,
    FishType.silver_salmon: 25,

    # Super rare fish
    FishType.gold_fish: 50,

    # Dev
    FishType.common_fish: 5,
    FishType.uncommon_fish: 10,
    FishType.rare_fish: 15,
    FishType.super_rare_fish: 25,
    FishType.legendary_fish: 100,
            
}

powerup_values = {
    Powerup.sake: 20,
    Powerup.coffee: 10,
    Powerup.gold_flakes: 75,
}

# Powerups

powerup_casts = {

    Powerup.sake: 10,
    Powerup.coffee: 15,
    Powerup.gold_flakes: 10,
}


# Crafting

recipes = {
    
    Powerup.gold_flakes: {FishType.gold_fish: 1}
}