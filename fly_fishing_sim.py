from time import sleep
from random import randint
from string import ascii_uppercase
from collections import Counter

main_menu_opts = ['Go fishing',
                  'See what fish you have',
                  'Go to the market',
                  'Change fly',
                  'Travel']

def menu(menu_text, options):

    # Printing menu
    print(menu_text)
    for item_num in range(len(options)):
        print(f'{list(ascii_uppercase)[item_num]}) {str(options[item_num]).capitalize()}')
        # Will print like "A) Brown trout"

    # Taking input and translating to list item
    while True:

        selection = input().upper().strip()
        selection_num = list(ascii_uppercase).index(selection)

        if selection not in list(ascii_uppercase):
            print('Invalid input! Enter only the letter corresponding to your selection.')
        
        elif selection_num > len(options) - 1:
            print('Invalid input! This letter does not correspond to an option.')
        
        else:
            return options[selection_num]
        

def go_fishing(fly,location):
    
    fish_caught = []

    odds = get_odds(fly)
    cast_time = get_time(fly)
    game = get_game(location)
    
    print(f'At {location}, you attach your {fly} fly to your fishing line and wade into the water.')
    print(f'Press [RETURN] to cast with your {fly} fly, or enter "LEAVE" to leave.')

    while True:
        
        # Check if leaving
        if input().upper().strip() == 'LEAVE':
            break

        print(f'You cast your line with your {fly} fly!')
    
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
    see_fish(fish_caught, 'You caught: ',"You didn't catch anything")
    
    return fish_caught


def market(money):
    
    print('Welcome to the market!')
    while True: 
        match menu('What would you like to do?', ['Visit shops','Sell fish','Leave']):
            
            case 'Visit shops':
                while True: 
                    match menu('Who would you like to visit?',['Template','Drink Lady','Fishmonger']):
                        
                        case 'Template':
                            print('Implementing soon!')
                        
                        case 'Drink Lady':
                            print('Implementing soon!')

                        case 'Fishmonger':
                            print('Implementing soon!')
                        
                        case _: 
                            print('Invalid option!')
            
            case 'Sell fish':  
                
                print("\nHere are today's prices:")
                for fsh in list(set(fish)):
                    print(f'- {fsh}: ${get_value(fsh)}')

                while True:
                    
                    fish_menu = {}
                    sell_opts = []

                    fish_counted = Counter(fish)
                    for fsh in fish_counted:

                        menu_key = f'{fsh} ({fish_counted[fsh]}x, ${get_value(fsh)} each)'

                        fish_menu.update({menu_key:fsh})
                        sell_opts.append(menu_key)
                        
                    sell_opts.extend(['Sell all', None])

                    sell_fish_selec = menu('What would you like to sell?', sell_opts)
                    
                    if sell_fish_selec:
                        
                        if sell_fish_selec == 'Sell all':
                            
                            add_money = 0
                            for fsh in fish:
                                fish.remove(fsh)
                                add_money += get_value(fsh)
                            
                            money += add_money
                            print(f'You sold all your fish for ${add_money}')
                            # Sold all as dev, it left behind 1 smallmouth, 1 brown trout, 1 steelhead, and 1 uncommon. Strange

                        while sell_fish_selec != 'Sell all':
                            
                            sell_fish = fish_menu.get(sell_fish_selec)

                            try: 
                                sell_num = int(input(f'How many {sell_fish} would you like to sell? (up to {fish.count(sell_fish)})\n'))
                                
                                if sell_num > fish.count(sell_fish):
                                    print("That's more than you have!")
                                
                                else:
                                    
                                    for num in range(sell_num):
                                        fish.remove(sell_fish)
                                    money += get_value(sell_fish) * sell_num

                                    print(f'You sold {sell_num} {sell_fish} for ${get_value(sell_fish) * sell_num}.')

                                    break

                            except ValueError:
                                print('Input only an integer (ex: 1)')

                    else: 
                        print(f'You now have ${money}')
                        break

            case 'Leave':
                return money
            
            case _: 
                print('Invalid option!')


def see_fish(fish, *text):

    if not fish:
        try: 
            print(text[1])
        except IndexError:
            print("You don't have any fish!")

    else: 
        fish_counted = Counter(fish)

        print(text[0])
        for fsh in fish_counted:
            print(f'- {fish_counted[fsh]} {fsh}')


def get_time(fly):
    
    fly_times = {
        
        # [0] = base time, +/- a randint beteen -1*[1] and [1]

        'white': [10,4],
        'red': [15,5],
        'gold': [7,3],

        'dev': [2,0],
        'dev_shit': [2,0],
    }
    return fly_times.get(fly, 0)


def get_odds(fly):
    
    fly_odds = {
        
        # [0]% chance to catch a common fish, [1]% chance for uncommon, [2]% for rare

        'white': [20,30,35],
        'red': [10,20,40],
        'gold': [50,70,80],

        'dev': [33,66,100],
        'dev_shit': [0,1,2],
    }
    return fly_odds.get(fly, 0)


def get_game(location):
    
    fish_pools = {
        'the dells': ['brown trout','smallmouth bass','muskellunge'],
        'chicago': ['brown trout','coho salmon','steelhead'],
        'dev': ['common','uncommon','rare']
    }
    
    return fish_pools.get(location, 0)


def get_value(fish):
    
    fish_values = {
        
        # Common fish
        'common': 5,
        'brown trout': 5,
        
        # Uncommon fish
        'uncommon': 7,
        'smallmouth bass': 7,
        'coho salmon': 8,

        # Rare fish
        'rare': 15,
        'muskellunge': 13, 
        'steelhead': 16,
        
    }

    return fish_values.get(fish, 0)
    

def main():

    flies = ['white']
    locations = ['the dells']

    global fish
    fish = []

    money = 0

    fly = flies[0]
    location = locations[0]

    # First fishing
    print('Welcome to fly fishing simulator!')
    if input('Press [ENTER] to go fishing.') == 'dev':
        
        # Optional dev mode

        flies = ['white','red','gold','dev','dev_shit']
        locations = ['the dells','chicago','dev']

        fly = 'dev'
        location = 'dev'

        for locat in locations:
            fish.extend(get_game(locat))
        money = 999

    fish.extend(go_fishing(fly,location))
    
    # Main menu
    while True:
        match menu('What would you like to do?', main_menu_opts):
            
            case 'Go fishing':
                fish.extend(go_fishing(fly,location))
            
            case 'See what fish you have':
                see_fish(fish, 'You have: ')

            case 'Go to the market':
                market(money)
            
            case 'Change fly':
                fly = menu('What fly would you like to use?', flies)
                print(f'You are now using your {fly} fly!')
            
            case 'Travel':
                location = menu('Where would you like to go?', locations)
                print(f'You are now at {location}!')
            
            case _: 
                print('Invalid option!')

main()