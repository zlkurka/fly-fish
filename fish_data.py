from enums import FishType, Location, Rarity

fish_pools = {

    Location.lake: {
        Rarity.common: [FishType.trout],
        Rarity.uncommon: [FishType.smallmouth],
        Rarity.rare: [FishType.muskellunge],
        Rarity.super_rare: [FishType.super_rare_fish],
    },
    Location.river: {
        Rarity.common: [FishType.trout],
        Rarity.uncommon: [FishType.salmon],
        Rarity.rare: [FishType.steelhead],
        Rarity.super_rare: [FishType.super_rare_fish],
    },
    Location.quarry: {
        Rarity.common: [FishType.steel_head],
        Rarity.uncommon: [FishType.uncommon_fish],
        Rarity.rare: [FishType.rare_fish],
        Rarity.super_rare: [FishType.gold_fish],
    },

    # Dev
    Location.dev: {
        Rarity.common: [FishType.common_fish],
        Rarity.uncommon: [FishType.uncommon_fish],
        Rarity.rare: [FishType.rare_fish],
        Rarity.super_rare: [FishType.super_rare_fish],
    },
}

fish_rarities = {
    Rarity.common: [FishType.trout],
    Rarity.uncommon: [FishType.smallmouth,FishType.salmon],
    Rarity.rare: [FishType.steelhead,FishType.muskellunge]
}

fish_values = {
            
    # Common fish
    FishType.trout: 5,
    
    # Uncommon fish
    FishType.smallmouth: 7,
    FishType.salmon: 8,

    # Rare fish
    FishType.muskellunge: 13, 
    FishType.steelhead: 16,
            
}

fish_materials = {}