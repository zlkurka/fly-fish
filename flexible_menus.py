from string import ascii_uppercase
from collections import Counter

from enums import FishType, Location, Fly, ItemType, Powerup

def menu(options=list, menu_text=str):

    # Printing menu
    print(menu_text)
    for item_num in range(len(options)):
        try:
            print(f'{ascii_uppercase[item_num]}) {options[item_num].value.capitalize()}')
        except AttributeError:
            print(f'{ascii_uppercase[item_num]}) {str(options[item_num]).capitalize()}')
        # Will print like "A) Squid"

    # Taking input and translating to list item
    while True:

        selection = input().upper().strip()

        if selection not in list(ascii_uppercase):
            print('Invalid input! Enter only the letter corresponding to your selection.')
        
        elif list(ascii_uppercase).index(selection) > len(options) - 1:
            print('Invalid input! This letter does not correspond to an option.')
        
        else:
            return options[list(ascii_uppercase).index(selection)]

def sell_menu(menu_text=str, items=dict, price=dict):

    menu_legend = {}
    sell_opts = []
    
    for sell_item in items:
        
        menu_key = f'{sell_item.value} ({items[sell_item]}x, ${price.get(sell_item)} each)'

        menu_legend.update({menu_key:sell_item})
        sell_opts.append(menu_key)
        
    sell_opts.extend(['Sell all', None])

    selection = menu(sell_opts, menu_text)
    
    if selection == None or selection == 'Sell all':
        return selection

    return menu_legend.get(selection)
    
def buy_menu(menu_text=str, items=list, price=dict):

    menu_legend = {}
    sell_opts = []
    
    items = Counter(items)
    for itm in items:
        
        menu_key = f"{itm.value} ({items[itm]}x, ${price[itm]} each)"

        menu_legend.update({menu_key:itm})
        sell_opts.append(menu_key)
        
    sell_opts.extend(['Buy all',None])

    selection = menu(sell_opts, menu_text)
    
    if not selection or selection == 'Buy all':
        return selection
    else:
        return menu_legend.get(selection)