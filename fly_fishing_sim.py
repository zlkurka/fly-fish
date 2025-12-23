from random import randint, choice
from collections import Counter
from time import sleep
from string import ascii_uppercase

from inventory import Inventory
from flexible_menus import menu, sell_menu, buy_menu
from enums import FishType, Location, Fly, ItemType, Rarity, Merchant
from fish_data import fish_pools, fish_rarities

def go_fishing(inventory=Inventory):
    
    fish_caught = []

    odds = inventory.get_odds()
    cast_time = inventory.get_time()
    game = inventory.get_game()

    print(f"At {inventory.location.value}, you attach your {inventory.fly.value} fly to your fishing line and wade into the water.")
    options = ['Change fly','Leave']

    # Fishing menu
    print('[RETURN]) Cast')
    for item_num in range(len(options)):
        print(f'{ascii_uppercase[item_num]}) {str(options[item_num]).capitalize()}')
        # Will print like "A) Change fly"

    # Taking input and translating to list item
    while True:

        selection = input().upper().strip()

        if selection == '':
            selection = 'Cast'
        elif selection not in ascii_uppercase:
            print('Invalid input! Enter only the letter corresponding to your selection.')
            continue
        elif ascii_uppercase.index(selection) > len(options) - 1:
            print('Invalid input! This letter does not correspond to an option.')
            continue
        else:
            selection = options[ascii_uppercase.index(selection)]
        
        match selection:
            case 'Cast':

                print(f"You cast your line with your {inventory.fly.value} fly!")

                # Sleeping for casting_time / 2, printing ellipsis every second
                for secs in range(cast_time[0] + randint(-1 * cast_time[1],cast_time[1])):
                    if secs // 2 != secs / 2:
                        print('...')
                    sleep(.5)

                # Determining catch
                fish_chance = randint(1,100)
                if fish_chance == 100:
                    fish = choice(game[Rarity.super_rare])
                elif odds[1] <= fish_chance < odds[2]:
                    fish = choice(game[Rarity.rare])
                elif odds[0] <= fish_chance < odds[1]:
                    fish = choice(game[Rarity.uncommon])
                elif fish_chance < odds[0]:
                    fish = choice(game[Rarity.common])
                else:
                    fish = None
                
                # Showing cast results
                if fish:
                    print(f"You caught a {fish.value}!")
                    fish_caught.append(fish)
                else:
                    print("It was just some seaweed.")
            
            case 'Change fly':
                inventory.change_fly()

            case 'Leave':
                
                # Display fish caught
                if not fish_caught:
                    print("You didn't catch anything")

                else: 
                    
                    fish_caught = Counter(fish_caught)

                    print('You caught:')
                    for fsh in fish_caught:
                        print(f"- {fish_caught[fsh]} {fsh.value}")

                    inventory.add_items(fish_caught, ItemType.fish)

                return inventory
            
            case _:
                print('Invalid selection!')


def market(inventory=Inventory):
    
    print('Welcome to the market!')
    while True: 
        match menu(['Visit shops','Sell fish','Leave'],'What would you like to do?'):
            
            case 'Visit shops':
                while True: 
                    match menu(['Fishmonger','Leave'],'Who would you like to visit?'):
                        
                        case 'Drink Lady':
                            print('Implementing soon!')

                        case 'Fishmonger':                            
                            
                            common_fish = fish_rarities[Rarity.common]
                            uncommon_fish = fish_rarities[Rarity.uncommon]
                            rare_fish = fish_rarities[Rarity.rare]

                            # Getting stock
                            stock = []
                            for iter in range(5):
                                
                                chance = randint(1,10)
                                
                                if 1 <= chance < 5:
                                    stock.append(choice(common_fish))
                                elif 5 <= chance < 10:
                                    stock.append(choice(uncommon_fish))
                                elif chance == 10:
                                    stock.append(choice(rare_fish))
                                
                                else:
                                    print('Failed to add fish')
                                    stock.append(FishType.trout)
                            
                            # Getting prices
                            prices = {}
                            for itm in stock:
                                if itm in prices:
                                    pass
                                elif itm in rare_fish:
                                    prices.update({itm:randint(15,19)})
                                elif itm in uncommon_fish:
                                    prices.update({itm:randint(7,10)})
                                elif itm in common_fish:
                                    prices.update({itm:randint(5,7)})
                                else: 
                                    print('Fish not found!')
                            
                            inventory, stock, prices = merchant(inventory, stock, prices, ['Could I interest you in anything from my collection?','Interested in anything else?'],'Okay, bye-bye!','You want everything? Wow... keep it up and there might be something in store for you.', Merchant.fishmonger) 
                        
                        case 'Leave':
                            break

                        case _: 
                            print('Invalid option!')
            

            case 'Sell fish':  
                
                if not inventory.fish:
                    print("You don't have any fish to sell!")
                    continue
                
                while inventory.fish:
                    
                    # Creating sell menu

                    fish_prices = {}
                    for itm in inventory.fish:
                        fish_prices.update({itm:inventory.get_value(itm)})

                    sell_fish = sell_menu('What would you like to sell?',inventory.fish,fish_prices)
                    
                    # Selling
                    
                    # None
                    if not sell_fish:
                        print(f"You now have ${inventory.money}")
                        break
                    
                    # Sell all
                    if sell_fish == 'Sell all':
                        
                        money_added = 0

                        for itm in list(inventory.fish):
                            
                            sell_num = inventory.fish.get(itm)

                            fish_worth = sell_num * inventory.get_value(itm)
                            money_added += fish_worth

                            inventory.remove_fish({itm:sell_num})
                        
                        inventory.change_money(money_added)

                        if inventory.fish:
                            print('Failed to remove all fish!')

                        print(f"You sold all your fish for ${money_added}")
                        break

                    # Particular fish selected
                    while sell_fish != 'Sell all':
                        
                        fish_num = inventory.fish.get(sell_fish)

                        try: 
                            sell_num = int(input(f"How many {sell_fish} would you like to sell? (up to {fish_num})\n").strip())
                            
                            if sell_num == 0:
                                print('Sale cancelled')
                                break

                            elif sell_num <= fish_num:

                                fish_worth = sell_num * inventory.get_value(sell_fish)
                                inventory.change_money(fish_worth)

                                inventory.remove_fish({sell_fish:sell_num})

                                print("You sold {sell_num} {sell_fish} for ${fish_worth}.")

                                break

                            else:
                                print("That's more than you have!")
                                
                        except ValueError:
                            print('Input only an integer (ex: 1)')
                    

            case 'Leave':
                return inventory
            
            case _: 
                print('Invalid option!')


def merchant(inventory=Inventory, stock=list, prices=dict, menu_txts=list, exit_text=str, buy_all_text=str, merchant_name=Merchant):
    
    match merchant_name:
        case Merchant.fishmonger:
            item_type = ItemType.fish

    menu_text = menu_txts[0]
    
    while True:

        buy_select = buy_menu(menu_text,stock,prices)
        
        # None
        if not buy_select:
            print(exit_text)
            return [inventory,stock,prices]
        
        # Buy all
        if buy_select == 'Buy all':

            money_subtracted = 0

            for itm in stock:
                money_subtracted += prices.get(itm)
            
            if money_subtracted > inventory.money:
                print("Insufficient funds!")
                return inventory


            for itm in list(stock):
                
                # Add sus fish
                if merchant_name == Merchant.fishmonger and randint(1,4) == 4:
                    inventory.add_items({itm:1}, ItemType.sus_fish)
                
                else:
                    inventory.add_items({itm:1}, item_type)
                
                stock.remove(itm)
                
            inventory.change_money(-1 * money_subtracted)

            if stock:
                print('Failed to buy all items!')
            
            print(f"You bought everything for ${money_subtracted}, and have ${inventory.money} left.")
            print(buy_all_text)
            return inventory, stock, prices
        
        # Buy one
        new_item_count = inventory.purchase(buy_select, stock.count(buy_select), prices.get(buy_select), ItemType.fish)

        for iter in range(stock.count(buy_select) - new_item_count):
            stock.remove(buy_select)
            if merchant_name == Merchant.fishmonger and randint(1,4) == 4:
                inventory.remove_fish({buy_select:1})
                inventory.add_items({buy_select:1}, ItemType.sus_fish)

        menu_text = menu_txts[1]


def main():
    
    inventory = Inventory()

    # First fishing
    print('Welcome to fly fishing simulator!')
    if input('Press [RETURN] to go fishing.') == 'dev':
        inventory.dev_mode()
    else:
        inventory = go_fishing(inventory)
    
    # Main menu
    while True:
        match menu(['Go fishing','Go to the market','Check inventory','Travel'], 'What would you like to do?'):
            
            case 'Go fishing':
                inventory = go_fishing(inventory)
            
            case 'Go to the market':
                market(inventory)

            case 'Check inventory':
                
                print(f"You have ${inventory.money}")
                match menu(['Fish','Flies','Locations','Powerups', 'Exit'],'What would you like to see?'):
                    
                    case 'Fish':
                        inventory.see_fish('You have:')
                    
                    case 'Exit':
                        continue

                    case _:
                        print('Invalid option!')
            
            case 'Travel':
                # location = menu(inventory.locations, 'Where would you like to go?')
                print(f"You are now at {inventory.location.value}!")
            
            case _: 
                print('Invalid option!')


main()