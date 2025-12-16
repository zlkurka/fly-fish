from random import randint
from collections import Counter
from time import sleep
from inventory import Inventory
from flexible_menu import menu

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
                    match menu(['Template','Drink Lady','Fishmonger'],'Who would you like to visit?'):
                        
                        case 'Template':
                            print('Implementing soon!')
                        
                        case 'Drink Lady':
                            print('Implementing soon!')

                        case 'Fishmonger':
                            print('Implementing soon!')
                        
                        case _: 
                            print('Invalid option!')
            
            case 'Sell fish':  

                while True:
                    
                    fish_menu = {}
                    sell_opts = []
                    
                    # Updating menu to include prices and the number of each fish you have
                    for fsh in inventory.fish:

                        menu_key = f'{fsh} ({inventory.fish[fsh]}x, ${inventory.get_value(fsh)} each)'

                        fish_menu.update({menu_key:fsh})
                        sell_opts.append(menu_key)
                        
                    sell_opts.extend(['Sell all', None])

                    sell_fish_selec = menu(sell_opts, 'What would you like to sell?')
                    

                    if sell_fish_selec:
                        
                        # Sell all
                        if sell_fish_selec == 'Sell all':
                            
                            money_added = 0
                            for fsh in inventory.fish:
                                
                                fish_worth = fsh.get(list(fsh)[0]) * inventory.get_price(fsh)
                                money_added += fish_worth

                                inventory.change_money(fish_worth)
                                fsh.remove_fish(fsh)

                            if inventory.fish:
                                print('Failed to remove all fish!')

                            print(f'You sold all your fish for ${money_added}')

                        # Particular fish selected
                        while sell_fish_selec != 'Sell all':
                            
                            sell_fish = fish_menu.get(sell_fish_selec)

                            try: 
                                sell_num = int(input(f'How many {sell_fish} would you like to sell? (up to {inventory.fish.get(sell_fish)})\n'))
                                
                                if sell_num > inventory.fish.get(sell_fish):
                                    print("That's more than you have!")
                                
                                else:
                                    
                                    fish_worth = inventory.fish.get(sell_fish_selec) * inventory.get_value(sell_fish_selec)
                                    fsh.get(list(fsh)[0]) * inventory.get_price(fsh)

                                    inventory.change_money(fish_worth)
                                    fsh.remove_fish(sell_fish_selec)

                                    for num in range(sell_num):
                                        inventory.remove_fish(sell_fish)
                                    money += inventory.get_value(sell_fish) * sell_num

                                    print(f'You sold {sell_num} {sell_fish} for ${inventory.get_value(sell_fish) * sell_num}.')

                                    break

                            except ValueError:
                                print('Input only an integer (ex: 1)')
                    
                    # None option
                    else: 
                        print(f'You now have ${money}')
                        break

            case 'Leave':
                return money
            
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
        match menu(main_menu_opts, 'What would you like to do?'):
            
            case 'Go fishing':
                inventory = go_fishing(inventory)
            
            case 'See what fish you have':
                inventory.see_fish('You have:')

            case 'Go to the market':
                market(inventory)
            
            case 'Change fly':
                inventory.change_fly()
                print(f'You are now using your {inventory.fly} fly!')
            
            case 'Travel':
                # location = menu(inventory.locations, 'Where would you like to go?')
                print(f'You are now at {inventory.location}!')
            
            case _: 
                print('Invalid option!')

main()