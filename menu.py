"""Provide user with a list of options."""

import pyinputplus as pyip

options_map = {
    1: ["option_a", "option_a.py",],
    2: ["option_b", "option_b.py",],
    3: ["exit", "",],
}

while True:
    print("\nPlease select from an option below.")
    for num, options in options_map.items():
        print(num, options[0])
    response = pyip.inputInt("> ", min=1, max=len(options_map))
    if response != 3:
        print(options_map[response][1])
    else:
        break
