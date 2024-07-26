"""Present user with options. Call function based on user selection."""

import pyinputplus as pyip
import functions

OPTIONS = (
    "func_a",
    "func_b",
    "exit"
)

OPTIONS_MAP = {}
NUM_OPTIONS = len(OPTIONS)

for num, option in enumerate(OPTIONS, 1):
    OPTIONS_MAP[num] = option

while True:
    print("\n")
    for num, option in OPTIONS_MAP.items():
        print(f"{num}. {option}")
    user_choice = pyip.inputInt("\nmake a selection\n> ", max=NUM_OPTIONS)
    if user_choice != NUM_OPTIONS:
        user_selected_func = OPTIONS_MAP[user_choice]
        method_to_call = getattr(functions, user_selected_func)
        method_to_call()
    else:
        print("\nsession complete\n")
        break
