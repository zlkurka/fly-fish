from random import randint, sample
from collections import Counter
from time import sleep
from inventory import Inventory
from flexible_menus import menu, sell_menu, buy_menu

def go_fishing(inventory=Inventory):
    
    fish_caught = []

    odds = inventory.get_odds()
    cast_time = inventory.get_time()
    game = inventory.get_game()

    print(f'At {inventory.location}, you attach your {inventory.fly} fly to your fishing line and wade into the water.')
    print(f'Press [RETURN] to cast, or enter "LEAVE" to leave.')

    while True:
        
        # Check if leaving
        if input().upper().strip() == 'LEAVE':
            break

        print(f'You cast your line with your {inventory.fly} fly!')
    
        casting_time = cast_time[0] + randint(-1 * cast_time[1],cast_time[1])

        # Sleeping for casting_time / 2, printing ellipsis every second
        print_ellipsis = True
        for secs in range(casting_time):
            print_ellipsis = not print_ellipsis
            if print_ellipsis:
                print('...')
            sleep(.5)

        # Determining catch
        fish_chance = randint(1,100)
        # Common
        if fish_chance < odds[0]:
            fish = game[0]
        # Uncommon
        elif odds[0] <= fish_chance < odds[1]:
            fish = game[1]
        # Rare
        elif odds[1] <= fish_chance < odds[2]:
            fish = game[2]
        else:
            fish = None
        
        # Showing cast results
        if fish:
            print(f'You caught a {fish}!')
            fish_caught.append(fish)
        else:
            print("It was just some seaweed.")
    
    # Display fish caught
    if not fish_caught:
        print("You didn't catch anything")

    else: 
        fish_counted = Counter(fish_caught)

        print('You caught:')
        for fsh in fish_counted:
            print(f'- {fish_counted[fsh]} {fsh}')

        inventory.add_items(fish_counted, 'fish')

    return inventory


def market(inventory=Inventory):
    
    print('Welcome to the market!')
    while True: 
        match menu(['Visit shops','Sell fish','Leave'],'What would you like to do?'):
            
            case 'Visit shops':
                while True: 
                    match menu(['Drink Lady','Fishmonger','Leave'],'Who would you like to visit?'):
                        
                        case 'Drink Lady':
                            print('Implementing soon!')

                        case 'Fishmonger':                            

                            common_fish = ['brown trout']
                            uncommon_fish = ['smallmouth bass','coho salmon']
                            rare_fish = ['steelhead','muskellunge']
                            
                            stock = []
                            for iter in range(5):
                                
                                chance = randint(1,10)
                                
                                # Common
                                if 1 <= chance < 5:
                                    stock.extend(sample(common_fish,1))
                                
                                # Uncommon
                                elif 5 <= chance < 10:
                                    stock.extend(sample(uncommon_fish,1))
                                
                                # Rare
                                elif chance == 10:
                                    stock.extend(sample(rare_fish,1))
                                
                                else:
                                    print('Failed to add fish')
                                    stock.append('brown trout')

                            stock = dict(Counter(stock))
                            
                            prices = {}
                            for itm in stock:
                                if itm in rare_fish:
                                    prices.update({itm:randint(7,10)})
                                elif itm in uncommon_fish:
                                    prices.update({itm:randint(7,10)})
                                elif itm in common_fish:
                                    prices.update({itm:randint(5,7)})
                                else: 
                                    print('Fish not found!')
                            
                            merch_output = merchant(inventory, stock, prices, ['Could I interest you in anything from my collection?','Interested in anything else?'],'Okay, bye-bye!',['You bought all my fish for $','!? Wow... keep it up and there might be something in store for you.'], 'fish') 
                            
                            inventory = merch_output[0]
                            stock = merch_output[1]
                            prices = merch_output[2]
                        
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
                        print(f'You now have ${inventory.money}')
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

                        print(f'You sold all your fish for ${money_added}')
                        break

                    # Particular fish selected
                    while sell_fish != 'Sell all':
                        
                        fish_num = inventory.fish.get(sell_fish)

                        try: 
                            sell_num = int(input(f'How many {sell_fish} would you like to sell? (up to {fish_num})\n'))
                            
                            if sell_num == 0:
                                print('Sale cancelled')
                                break

                            elif sell_num <= fish_num:

                                fish_worth = sell_num * inventory.get_value(sell_fish)
                                inventory.change_money(fish_worth)

                                inventory.remove_fish({sell_fish:sell_num})

                                print(f'You sold {sell_num} {sell_fish} for ${fish_worth}.')

                                break

                            else:
                                print("That's more than you have!")
                                
                        except ValueError:
                            print('Input only an integer (ex: 1)')
                    

            case 'Leave':
                return inventory
            
            case _: 
                print('Invalid option!')


def merchant(inventory=Inventory, stock=dict, prices=dict, menu_txts=list, exit_text=str, buy_all_text=str, item_type=str):
    
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

            for itm in list(stock):
                money_subtracted += stock.get(itm) * prices.get(itm)
            
            if money_subtracted > inventory.money:
                print("Insufficient funds!")
                return inventory

            for itm in list(stock):
                inventory.add_items({itm:stock.get(itm)}, item_type)
                stock.pop(itm)
                
            inventory.change_money(money_subtracted)

            if stock:
                print('Failed to buy all items!')

            print(buy_all_text[0], money_subtracted, buy_all_text[1])
            return [inventory,stock,prices]
        
        # Buy one
        new_item_count = inventory.purchase(buy_select, stock.get(buy_select), prices.get(buy_select))
        
        if new_item_count == 0:
            stock.pop(buy_select)
            prices.pop(buy_select)
        else:
            stock.update({buy_select:new_item_count})

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
        match menu(['Go fishing','Go to the market','Check inventory','Change fly','Travel'], 'What would you like to do?'):
            
            case 'Go fishing':
                inventory = go_fishing(inventory)
            
            case 'Go to the market':
                market(inventory)

            case 'Check inventory':
                
                print(f'You have ${inventory.money}')
                match menu(['Fish','Flies','Locations','Powerups', 'Exit'],'What would you like to see?'):
                    
                    case 'Fish':
                        inventory.see_fish('You have:')
                    
                    case 'Exit':
                        continue

                    case _:
                        print('Invalid option!')
            
            case 'Change fly':
                inventory.change_fly()
                print(f'You are now using your {inventory.fly} fly!')
            
            case 'Travel':
                # location = menu(inventory.locations, 'Where would you like to go?')
                print(f'You are now at {inventory.location}!')
            
            case _: 
                print('Invalid option!')


main()