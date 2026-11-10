import game_data
import random
import art
score = 0
index = 0
choice = ""

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f'{BOLD}{MAGENTA}{art.logo}{RESET}')
print(f'{BOLD}{CYAN}Welcome the "Higher/Lower" Game!!!\nIn this game you will have to guess whether the following object has higher or lower number of monthly inquiries!{RESET}')
print(f'{BOLD}{YELLOW}GOOD LUCK!\n*****************************************************************************************************************{RESET}')

#Shuffling of the elements in the game_data list.
shuffled = []
for i in range(len(game_data.data)):
    shuffled.append(game_data.data.pop(random.randint(0, len(game_data.data) - 1)))

#Game engine
for index in range(len(shuffled) - 1):
    former = shuffled[index]['follower_count']
    latter = shuffled[index + 1]['follower_count']

    name_former = shuffled[index]['name']
    name_latter = shuffled[index + 1]['name']

    description_former = shuffled[index]['description']
    description_latter = shuffled[index + 1]['description']

    country_former = shuffled[index]['country']
    country_latter = shuffled[index + 1]['country']

    print(f"{name_former}, {description_former} from {country_former} has {RED}{former}{RESET} monthly "
          f"inquiries.\n\nDo you think that {name_latter}, {description_latter} from "
          f"{country_latter} has higher or lower number of inquiries? ")

    choice = input("\nWhat's your guess (higher/lower): ").lower()
    while choice not in ["higher", "lower"]:
        choice = input("Only \"higher\" or \"lower\" is allowed input. Please retry your entry:\n").lower()
    if former > latter and choice == "lower":
        print("\n" * 10 + f'Correct! {name_latter} has {RED}{latter}{RESET} inquiries which is lower than {RED}{former}{RESET}')
        score += 1
    elif former < latter and choice == "higher":
        print("\n" * 10 + f'Correct! {name_latter} has {RED}{latter}{RESET} inquiries which is higher than {RED}{former}{RESET}')
        score += 1
    else:
        break

print(f'{RED}Game Over!{RESET}Your score is {GREEN}{score}{RESET}!')

