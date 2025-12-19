from enums import FishType, Rarity, Location

class Fish:

    fish_name: FishType
    is_sus: bool

    fish_pools = {
        Location.dells: [FishType.trout,FishType.smallmouth,FishType.muskellunge],
        Location.chicago: [FishType.trout,FishType.salmon,FishType.steelhead],
        Location.dev: [FishType.common_fish,FishType.uncommon_fish,FishType.rare_fish]
        }
    
    def __init__(self, name=FishType, *sus):
        
        # Add name
        self.fish_name = name

        # Add sus
        if sus:
            self.is_sus = True
        else:
            self.is_sus = False

    def get_game(self, location=Location):
        return self.fish_pools[location]

    def get_name(self):
        if self.is_sus:
            return 'suspicious ' + self.fish_name.value
        else:
            return self.fish_name.value
        
    def get_rarity(self):
        if self.fish_name in [FishType.trout,FishType.common_fish]:
            return Rarity.common
        elif self.fish_name in [FishType.smallmouth,FishType.salmon,FishType.uncommon_fish]:
            return Rarity.uncommon
        elif self.fish_name in [FishType.steelhead,FishType.muskellunge,FishType.rare_fish]:
            return Rarity.rare
        else:
            print('Fish rarity not found!')
            return None
    
    def get_pools(self):
        
        pools = []

        for location in self.fish_pools:
            if self.fish_name in self.fish_pools[location]:
                pools.append(location)
        
        return pools

    def get_materials(self):
        # Use sus
        pass


def testing():

    new_fish = Fish(FishType.trout)
    print(new_fish.get_name())

    sus_fish = Fish(FishType.salmon, True)
    print(sus_fish.get_name())