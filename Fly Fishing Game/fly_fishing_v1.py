from time import sleep
from random import randint
from string import ascii_uppercase
from collections import Counter

# Last modified November 24th, 2025

def go_fish(fly,location):
    
    cooler = []
    game = get_game(location)

    print(f'Press [RETURN] to cast with your {fly} fly, or enter "LEAVE" to leave.')

    while True:
        
        check_exit = input()
        if check_exit.upper() == 'LEAVE':
            break
        
        cast_line(fly)
        fish = catch_fish(get_odds(fly))
        
        if fish:
            print(f'You caught a {game[int(fish)]}!')
            cooler.append(game[int(fish)])
        else:
            print("It was just some seaweed.")
        
    if not cooler:
        print("You didn't catch anything today.")
        return None
    
    fish_caught = Counter(cooler)

    print('You caught:')
    for fish in fish_caught:
        print(f'- {fish_caught[fish]} {fish}')
    
    return cooler

def get_time(fly):
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
        
def cast_line(fly):
    print(f'You cast your line with your {fly} fly!')
    
    fly_times = get_time(fly)
    
    casting_time = fly_times[0] + randint(-1 * fly_times[1],fly_times[1])

    print_ellipsis = True
    for secs in range(casting_time):
        print_ellipsis = not print_ellipsis
        if print_ellipsis:
            print('...')
        sleep(.5)

def get_game(location):
    
    match location:
        case 'the dells':
            return ['brown trout','smallmouth bass','muskellunge']
        case 'chicago':
            return ['brown trout','coho salmon','steelhead']
        case _:
            print('Invalid location!')
            return None

def catch_fish(odds):

    fish_chance = randint(1,100)

    if fish_chance < odds[0]:
        return '0'
    elif odds[0] <= fish_chance < odds[1]:
        return 1
    elif odds[1] <= fish_chance < odds[2]:
        return 2
    else:
        return None

def main():
    
    flies = ['white','red','gold','dev','dev_shit']
    fish_caught = []

    fly = flies[3]
    location = 'the dells'
    
    print('Welcome to fly fishing simulator!')
    sleep(.5)

    while True:
        go_to = input('What would you like to do?\n'
                      'A) Go fishing\n'
                      'B) See what fish you have\n'
                      'C) Go shopping\n'
                      'D) Sell fish\n'
                      'E) Change fly\n'
                      'F) Travel\n')
        match go_to.upper():
            case 'A':
                fish_caught.extend(go_fish(fly,location))
            case 'B':
                fish_counted = Counter(fish_caught)

                print('You caught:')
                for fish in fish_counted:
                    print(f'- {fish_counted[fish]} {fish}')
    
            case 'C':
                print('Implementing soon!')
            case 'D':
                print('Implementing soon!')
            case 'E':
                print('What fly would you like to use?')
                for x in range(len(flies)):
                    print(f'{list(ascii_uppercase)[x]}) {flies[x].capitalize()}')
                new_fly = input()
                fly = flies[list(ascii_uppercase).index(new_fly.upper())]
                print(f'You are now using your {fly} fly!')
            case 'F':
                location = None
                while not location:
                    new_location = input('Where would you like to go?\nA) The Dells\nB) Chicago\n')
                    match new_location.upper():
                        case 'A':
                            location = 'the dells'
                        case 'B':
                            location = 'chicago'
                        case _:
                            print('Invalid option!')
                            location = None
            case _: 
                print('Invalid option!')

main()