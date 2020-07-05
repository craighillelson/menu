"""Provide user with a list of options."""

import pyinputplus as pyip

options = {
    1: 'option_1.py',
    2: 'option_2.py',
    3: 'option_3.py',
    }


def switch_case(argument):
    """Switch case statement."""
    options
    return options.get(argument, 'nothing')


while True:
    print('\nMake a selection or press enter to quit')
    for num, option in options.items():
        print(num, option)
    selection = pyip.inputInt('> ', min=1, max=len(options), blank=True)
    if selection != '':
        print(switch_case(selection))
        # replace with code below to call python files
        # exec(open(switch_case(selection)).read())
    else:
        print('\nSession complete.\n')
        break
