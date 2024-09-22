# 1. Function to roll call the dwarves
def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")

# 2. Function to summon Captain Planet (capitalize and add exclamation marks)
def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]

# 3. Function to check if there are long planeteer calls (longer than 4 characters)
def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

# 4. Function to find the cheese in a list
def find_the_cheese(foods):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheese_types:
            return food
    return None
