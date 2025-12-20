from enums import FishType, Location, Rarity

fish_pools = {
    Location.dells: [FishType.trout,FishType.smallmouth,FishType.muskellunge],
    Location.chicago: [FishType.trout,FishType.salmon,FishType.steelhead],
}

fish_rarities = {
    Rarity.common: [FishType.trout],
    Rarity.uncommon: [FishType.smallmouth,FishType.salmon],
    Rarity.rare: [FishType.steelhead,FishType.muskellunge]
}

fish_materials = {}