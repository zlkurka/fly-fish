from string import ascii_uppercase

def menu(options, menu_text):

    # Printing menu
    print(menu_text)
    for item_num in range(len(options)):
        print(f'{list(ascii_uppercase)[item_num]}) {str(options[item_num]).capitalize()}')
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

def sell_menu(menu_text, items, price):

    menu_legend = {}
    sell_opts = []
    
    for sell_item in items:
        
        menu_key = f'{sell_item} ({items[sell_item]}x, ${price.get(sell_item)} each)'

        menu_legend.update({menu_key:sell_item})
        sell_opts.append(menu_key)
        
    sell_opts.extend(['Sell all', None])

    selection = menu(sell_opts, menu_text)
    
    if selection == None or selection == 'Sell all':
        return selection

    return menu_legend.get(selection)
    
def buy_menu(menu_text, items, price):

    menu_legend = {}
    sell_opts = []
    
    for sell_item in items:
        
        menu_key = f'{sell_item} ({items[sell_item]}x, ${price[sell_item]} each)'

        menu_legend.update({menu_key:sell_item})
        sell_opts.append(menu_key)
        
    sell_opts.extend(['Buy all',None])

    selection = menu(sell_opts, menu_text)
    
    if not selection or selection == 'Buy all':
        return selection
    else:
        return menu_legend.get(selection)