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