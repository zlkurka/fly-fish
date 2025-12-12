from time import sleep
from random import randint
from string import ascii_uppercase
from collections import Counter

main_menu_opts = ['Go fishing',
                  'See what fish you have',
                  'Go shopping',
                  'Sell fish',
                  'Change fly',
                  'Travel']

def menu(options, menu_text):

    # Printing menu
    print(menu_text)
    for item_num in range(len(options)):
        print(f'{list(ascii_uppercase)[item_num]}) {options[item_num].capitalize()}')
        # Will print like "A) Squid"

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
        
def go_fish(fly,location):
    
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
    if not fish_caught:
        print("You didn't catch anything.")
    else: 
        show_fish = Counter(fish_caught)
        print('You caught:')
        for fish in show_fish:
            print(f'- {show_fish[fish]} {fish}')
    
    return fish_caught

def get_time(fly):
    
    # [0] = base time, +/- a randint beteen -1*[1] and [1]

    match fly:
        case 'white':
            return [10,4]
        case 'red':
            return [15,5]
        case 'gold':
            return [7,3]
        case 'dev':
            return [2,0]
        case 'dev_shit':
            return [2,0]
        case _:
            print('Invalid fly!')
            return None

def get_odds(fly):
    
    # [0]% chance to catch a common fish, [1]% chance for uncommon, [2]% for rare

    match fly:
        case 'white':
            return [20,30,35]
        case 'red':
            return [10,20,40]
        case 'gold':
            return [50,70,80]
        case 'dev':
            return [33,66,100]
        case 'dev_shit':
            return [0,1,2]
        case _:
            print('Invalid fly!')
            return None
        
def get_game(location):
    
    match location:
        case 'the dells':
            return ['brown trout','smallmouth bass','muskellunge']
        case 'chicago':
            return ['brown trout','coho salmon','steelhead']
        case 'dev':
            return ['common','uncommon','rare']
        case _:
            print('Invalid location!')
            return None
        
def main():

    flies = ['white']
    locations = ['the dells']
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

    fish.extend(go_fish(fly,location))
    
    # Main menu
    while True:
        match menu(main_menu_opts, 'What would you like to do?'):
            
            case 'Go fishing':
                fish.extend(go_fish(fly,location))
            
            case 'See what fish you have':
                
                if not fish:
                    print("You don't have any fish!")
                else: 
                    fish_counted = Counter(fish)

                    print('You have:')
                    for fsh in fish_counted:
                        print(f'- {fish_counted[fsh]} {fsh}')

            case 'Go shopping':
                print('Implementing soon!')
            
            case 'Sell fish':
                print('Implementing soon!')
            
            case 'Change fly':
                fly = menu(flies,'What fly would you like to use?')
                print(f'You are now using your {fly} fly!')
            
            case 'Travel':
                location = menu(locations,'Where would you like to go?')
                print(f'You are now at {location}!')
            
            case _: 
                print('Invalid option!')

main()