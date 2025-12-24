from string import ascii_uppercase
from collections import Counter

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

def counting_menu(items, menu_text=str, *prices):
    
    menu_legend = {}
    options = []
    
    if type(items) == list:
        items = Counter(items)
    
    # Assembling menu
    for itm in items:
        
        if prices:
            menu_key = f'{itm.value} ({items[itm]}x, ${prices[0][itm]} each)'
        else:
            menu_key = f'{itm.value} ({items[itm]}x)'

        menu_legend.update({menu_key: itm})
        options.append(menu_key)
        
    if len(items) > 1:
        options.append('All')
    options.append(None)

    selection = menu(options, menu_text)
    
    if selection == None or selection == 'All':
        return selection

    return menu_legend[selection]