from random import randint, sample
from collections import Counter
from time import sleep
from inventory import Inventory
from flexible_menu import menu, sell_menu, buy_menu

main_menu_opts = ['Go fishing',
                  'See what fish you have',
                  'Go to the market',
                  'Change fly',
                  'Travel']

def go_fishing(inventory):
    
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
    if not fish:
        print("You didn't catch anything")


    else: 
        fish_counted = Counter(fish_caught)

        print('You caught:')
        for fsh in fish_counted:
            print(f'- {fish_counted[fsh]} {fsh}')

        inventory.add_fish(fish_counted)

    return inventory


def market(inventory):
    
    print('Welcome to the market!')
    while True: 
        match menu(['Visit shops','Sell fish','Leave'],'What would you like to do?'):
            
            case 'Visit shops':
                while True: 
                    match menu(['Drink Lady','Fishmonger'],'Who would you like to visit?'):
                        
                        case 'Drink Lady':
                            print('Implementing soon!')

                        case 'Fishmonger':                            

                            common_fish = ['brown trout']
                            uncommon_fish = ['smallmouth bass','coho salmon']
                            rare_fish = ['steelhead','muskellunge']
                            
                            fish_options = []
                            for iter in range(5):
                                
                                chance = randint(1,10)
                                
                                # Common
                                if 1 <= chance < 5:
                                    fish_options.extend(sample(common_fish,1))
                                
                                # Uncommon
                                elif 5 <= chance < 10:
                                    fish_options.extend(sample(uncommon_fish,1))
                                
                                # Rare
                                elif chance == 10:
                                    fish_options.extend(sample(rare_fish,1))
                                
                                else:
                                    print('Failed to add fish')
                                    fish_options.append('brown trout')

                            fish_options = dict(Counter(fish_options))
                            
                            prices = {}
                            for fsh in fish_options:
                                if fsh in rare_fish:
                                    prices.update({fsh:randint(7,10)})
                                elif fsh in uncommon_fish:
                                    prices.update({fsh:randint(7,10)})
                                elif fsh in common_fish:
                                    prices.update({fsh:randint(5,7)})
                                else: 
                                    print('Fish not found!')
                            
                            menu_text = 'Could I interest you in anything from my collection?'
                            while True:
                                sell_select = buy_menu(menu_text,fish_options,prices)
                                if not sell_select:
                                    print('Okay, bye-bye!')
                                    break
                                new_item_count = inventory.purchase(sell_select, fish_options.get(sell_select), prices.get(sell_select))
                                
                                if new_item_count == 0:
                                    fish_options.pop(sell_select)
                                    prices.pop(sell_select)
                                else:
                                    fish_options.update({sell_select:new_item_count})

                                menu_text = 'Interested in anything else?'
                        
                        case _: 
                            print('Invalid option!')
            

            case 'Sell fish':  
                
                if not inventory.fish:
                    print("You don't have any fish to sell!")
                    continue
                
                while True:
                    
                    # Creating sell menu

                    fish_prices = {}
                    for fsh in inventory.fish:
                        fish_prices.update({fsh:inventory.get_value(fsh)})

                    sell_fish = sell_menu('What would you like to sell?',inventory.fish,fish_prices)
                    
                    # Selling
                    
                    # None
                    if not sell_fish:
                        print(f'You now have ${inventory.money}')
                        break
                    
                    # Sell all
                    if sell_fish == 'Sell all':
                        
                        money_added = 0

                        for fsh in list(inventory.fish):
                            
                            sell_num = inventory.fish.get(fsh)

                            fish_worth = sell_num * inventory.get_value(fsh)
                            money_added += fish_worth

                            inventory.remove_fish({fsh:sell_num})
                        
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


def main():
    
    inventory = Inventory()

    # First fishing
    print('Welcome to fly fishing simulator!')
    if input('Press [ENTER] to go fishing.') == 'dev':
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
                match menu(['Fish','Flies','Locations','Powerups', 'Exit']):
                    
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