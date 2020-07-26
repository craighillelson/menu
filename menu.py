"""Provide user with a list of options."""

import pyinputplus as pyip

# populate list with available choices
choices = ['option 1', 'option 2', 'quit']

while True:
    print('\nPlease select from the options below.')
    for num, choice in enumerate(choices, 1):
        print(num, choice)
    selection = pyip.inputMenu(choices, prompt='> ', blank=True, numbered=True)
    if selection != 'quit':
        print(f'You selected {selection}')
    else:
        break
