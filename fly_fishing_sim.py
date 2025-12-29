from random import randint, choice
from collections import Counter
from time import sleep
from string import ascii_uppercase
from decimal import Decimal, ROUND_HALF_UP

from inventory import Inventory
from flexible_menus import menu, counting_menu
from enums import FishType, Powerup, Rarity, Merchant
from fish_data import fish_rarities, fish_values, powerup_values


def go_fishing(inventory=Inventory):
    
    fish_caught = []
    pups_in_use = {}

    common_odds, uncommon_odds, rare_odds = inventory.get_odds()
    cast_time = inventory.get_time()
    game = inventory.get_game()
    rarities = [Rarity.common,Rarity.uncommon,Rarity.rare,Rarity.super_rare]

    print(f"At {inventory.location.value}, you attach your {inventory.fly.value} fly to your fishing line and wade into the water.")
    options = ['Leave']
    
    if inventory.powerups:
        options.insert(0, 'Use a powerup')
    if len(inventory.flies) > 1:
        options.insert(0, 'Change fly')

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
                    fish = choice(game[rarities[3]])
                elif uncommon_odds < fish_chance <= rare_odds:
                    fish = choice(game[rarities[2]])
                elif common_odds < fish_chance <= uncommon_odds:
                    fish = choice(game[rarities[1]])
                elif fish_chance <= common_odds:
                    fish = choice(game[rarities[0]])
                else:
                    fish = None
                
                # Showing cast results
                if fish:
                    print(f"You caught a {fish.value}!")
                    fish_caught.append(fish)
                else:
                    print("It was just some seaweed.")
                
                # Powerup upkeep
                for pup in list(pups_in_use):
                    remaining_casts = pups_in_use[pup] - 1
                    if remaining_casts:
                        pups_in_use.update({pup: remaining_casts})
                    else:
                        pups_in_use.pop(pup)
                        print(f'Your {pup.value} wears off.')
                        
                        match pup:
                            case Powerup.sake:
                                common_odds, uncommon_odds, rare_odds = inventory.get_odds()
                            case Powerup.coffee:
                                cast_time = inventory.get_time()
                            case Powerup.gold_flakes:
                                rarities = [Rarity.common,Rarity.uncommon,Rarity.rare,Rarity.super_rare]
                            case _:
                                print(f"{pup} wear-off not found!")

            case 'Change fly':
                inventory.change_fly()
            
            case 'Use a powerup':
                added_pups = inventory.use_powerup(pups_in_use)
                pups_in_use.update(added_pups)

                for pup in added_pups:

                    match pup:
                        case Powerup.sake:
                            
                            # All odds += 5
                            common_odds += 5
                            uncommon_odds += 10
                            rare_odds += 15

                        case Powerup.coffee:
                            
                            ct_base = cast_time[0] - 2
                            if ct_base < 0:
                                ct_base = 0
                            ct_variance = cast_time[1] -2
                            if ct_variance < 0:
                                ct_variance = 0

                            cast_time = [ct_base, ct_variance]
                        
                        case Powerup.gold_flakes:
                            rarities = [Rarity.uncommon,Rarity.rare,Rarity.super_rare,Rarity.legendary]
                        
                        case _:
                            print(f'{pup.value.capitalize()} effects unknown!')

            case 'Leave':
                
                # Display fish caught
                if not fish_caught:
                    print("You didn't catch anything")

                else: 
                    
                    fish_caught = dict(Counter(fish_caught))

                    print('You caught:')
                    for fsh in fish_caught:
                        print(f"- {fish_caught[fsh]} {fsh.value}")

                    for fsh in fish_caught:
                        inventory.add_items({fsh: fish_caught[fsh]})

                return inventory
            
            case _:
                print('Invalid selection!')


def market(inventory=Inventory):
    
    visits = {
        Merchant.drink_lady: False,
        Merchant.fishmonger: False,
    }

    print('Welcome to the market!')
    while True: 
        match menu(['Visit shops','Sell fish','Leave'],'What would you like to do?'):
            
            case 'Visit shops':
                while True: 
                    match menu(['Drink Lady','Fishmonger','Leave'],'Who would you like to visit?'):
                        
                        case 'Drink Lady':
                            
                            if not visits[Merchant.drink_lady]:
                                stock = []
                                for iter in range(randint(1,3)):
                                    stock.append(Powerup.sake)
                                for iter in range(randint(2,5)):
                                    stock.append(Powerup.coffee)

                                if randint(1,10) == 10:
                                    stock.append(Powerup.gold_flakes)
                                
                                prices = get_prices(stock, 1.6)
                                
                                visits.update({Merchant.drink_lady: True})
                            
                            if not stock:
                                print("Sorry, carissima, I have nothing left today.")
                                continue

                            inventory, stock, prices = merchant(inventory, stock, prices, ['Thirsty?','Craving anything else?'],'Arrivederci...','Try not to waste it...''.', Merchant.drink_lady) 


                        case 'Fishmonger':                            
                            
                            if not visits[Merchant.fishmonger]:
                                # Getting stock
                                stock = []
                                for iter in range(5):
                                    
                                    chance = randint(1,10)
                                    
                                    if 1 <= chance < 5:
                                        stock.append(choice(fish_rarities[Rarity.common]))
                                    elif 5 <= chance < 10:
                                        stock.append(choice(fish_rarities[Rarity.uncommon]))
                                    elif chance == 10:
                                        stock.append(choice(fish_rarities[Rarity.rare]))
                                    
                                    else:
                                        print('Failed to add fish')
                                        stock.append(FishType.trout)
                                
                                # Getting prices
                                prices = get_prices(stock, 1.7)
                                
                                visits.update({Merchant.fishmonger: True})
                            
                            if not stock:
                                print("Sorry, you've taken all I have to offer today.")
                                continue
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
                        try:
                            fish_prices.update({itm: fish_values[itm]})
                        except KeyError:
                            print(f'{itm.value.capitalize()} value not found!')
                            fish_prices.update({itm: 0})

                    sell_fish = counting_menu(inventory.fish, 'What would you like to sell?', fish_prices)
                    
                    # Selling
                    
                    # None
                    if not sell_fish:
                        print(f"You now have ${inventory.money}")
                        break
                    
                    # Sell all
                    if sell_fish == 'All':
                        
                        money_added = 0

                        for itm in list(inventory.fish):
                            
                            sell_num = inventory.fish.get(itm)

                            fish_worth = sell_num * inventory.get_value(itm)
                            money_added += fish_worth

                            inventory.remove_items({itm: sell_num})
                        
                        inventory.change_money(money_added)

                        if inventory.fish:
                            print('Failed to remove all fish!')

                        print(f"You sold all your fish for ${money_added}")
                        break

                    # Particular fish selected
                    while sell_fish != 'All':
                        
                        fish_num = inventory.fish[sell_fish]

                        try: 
                            sell_num = int(input(f"How many {sell_fish.value} would you like to sell? (up to {fish_num})\n").strip())
                            
                        except ValueError:
                            print('Input only an integer (ex: 1)')
                            continue

                        if sell_num == 0:
                            print('Sale cancelled')
                            break

                        if sell_num > fish_num:
                            print("That's more than you have!")
                            continue

                        fish_worth = sell_num * inventory.get_value(sell_fish)
                        inventory.change_money(fish_worth)

                        inventory.remove_items({sell_fish: sell_num})

                        print(f"You sold {sell_num} {sell_fish.value} for ${fish_worth}.")

                        break

            case 'Leave':
                return inventory
            
            case _: 
                print('Invalid option!')


def merchant(inventory=Inventory, stock=list, prices=dict, menu_txts=list, exit_text=str, buy_all_text=str, merchant_name=Merchant):
    
    match merchant_name:
        case Merchant.fishmonger:
            item_type = FishType

    menu_text = menu_txts[0]
    
    while True:

        buy_select = counting_menu(stock, menu_text, prices)
        
        # None
        if not buy_select:
            print(exit_text)
            return inventory, stock, prices
        
        # Buy all
        if buy_select == 'All':

            money_subtracted = 0

            for itm in stock:
                money_subtracted += prices.get(itm)
            
            if money_subtracted > inventory.money:
                print("Insufficient funds!")
                return inventory, stock, prices


            for itm in list(stock):
                
                # Add sus fish
                if merchant_name == Merchant.fishmonger and randint(1,4) == 4:
                    inventory.add_items({itm: 1}, True)
                
                else:
                    inventory.add_items({itm: 1})
                
                stock.remove(itm)
                
            inventory.change_money(-1 * money_subtracted)

            if stock:
                print('Failed to buy all items!')
            
            print(f"You bought everything for ${money_subtracted}, and have ${inventory.money} left.")
            print(buy_all_text)
            return inventory, stock, prices
        
        # Buy one
        new_item_count = inventory.purchase(buy_select, stock.count(buy_select), prices.get(buy_select))

        for iter in range(stock.count(buy_select) - new_item_count):
            stock.remove(buy_select)
            if merchant_name == Merchant.fishmonger and randint(1,4) == 4:
                inventory.remove_items({buy_select:1})
                inventory.add_items({buy_select:1}, True)

        menu_text = menu_txts[1]


def get_prices(stock=list, max_prop=float):
    
    if FishType == type(stock[0]):
        values = fish_values
    elif Powerup == type(stock[0]):
        values = powerup_values
    
    prices = {}
    for itm in stock:
        if itm in prices:
            continue
        elif itm in values:
            prices.update({itm: int(Decimal(values[itm] * (1 + (randint(0, int((max_prop - 1) * 10)) / 10))).quantize(1, rounding=ROUND_HALF_UP))})
        else:
            print(f'{itm.value.capitalize()} value not found!')
    return prices


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
        
        menu_opts = ['Go fishing','Go to the market','Check inventory','End the day','Exit game']
        if len(inventory.locations) > 1:
            menu_opts.insert(3, 'Travel')
        
        match menu(menu_opts, 'What would you like to do?'):
            
            case 'Go fishing':
                inventory = go_fishing(inventory)
            
            case 'Go to the market':
                market(inventory)

            case 'Check inventory':
                inventory.check_inv()
            
            case 'Travel':
                inventory.travel()

            case 'End the day':
                print('Implementing soon!')
            
            case 'Exit game':
                match menu(['Leave','Keep playing'], "Are you sure you'd like to exit?"):

                    case 'Leave':
                        print('Thanks for playing!')
                        exit()

                    case 'Keep playing':
                        continue

                    case _:
                        print('Invalid option!')
            
            case _: 
                print('Invalid option!')


main()