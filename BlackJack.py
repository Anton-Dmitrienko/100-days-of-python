import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
         "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]

shuffled_deck = []
for i in range(52):
    shuffled_deck.append(cards.pop(random.randint(0, len(cards)-1)))
player_hand = []
dealer_hand = []
player_count = 0
dealer_count = 0

print(logo)

#Pick_card function definition: pick No cards from the deck and add them to the hand.
def pick_card(number, hand):
    for i in range(number):
        hand.append(shuffled_deck.pop(0))
    return hand

def calculate(hand):
    count = 0

    aces = hand.count("A")
    for value in hand:
        if value == "A":
            count += 11
        elif type(value) == str:
            count +=10
        else:
            count += value
    while count > 21:
        if aces > 0:
            count -= 10
            aces -= 1
        else:
            break
    return count

def player_plays():
    player_count = calculate(player_hand)
    pick = input("Would you like to pick another card? (y/n?)")
    while pick == "y":
        pick_card(1, player_hand)
        print(f"Your hand is {player_hand}")
        player_count = calculate(player_hand)
        if player_count < 21:
            print(f"Your current count is {player_count}")
            pick = input("Would you like to pick another card? (y/n?)")
        elif player_count == 21:
            print(f"Your current count is {player_count}")
            break
        else:
            break
    return player_count

def dealer_plays():
    dealer_count = calculate(dealer_hand)
    while calculate(dealer_hand) < 17:
        pick_card(1, dealer_hand)
        dealer_count = calculate(dealer_hand)
    print(f"Dealer's hand is {dealer_hand}")
    print(f"Your hand is {player_hand}")
    return dealer_count


#Distribute two cards to the player's and dealer's hand.
pick_card(2, dealer_hand)
dealer_count = calculate(dealer_hand)
print(f"The open card in dealer's hand is {dealer_hand[0]}")

pick_card(2, player_hand)
player_count = calculate(player_hand)
print(f"Your hand is {player_hand}")
print(player_count)

if player_count == 21 and dealer_count == 21:
    print(f"IT'S THE DRAW!")
elif player_count == 21 and dealer_count != 21:
    print(f"YOU WON!")
elif player_count != 21 and dealer_count == 21:
    print(f"The dealer's hand is {dealer_hand}")
    print(f"YOU LOST due to natural BlackJack!")
elif player_count != 21 and dealer_count != 21:
    player_count = player_plays()
    if player_count <= 21:
        dealer_count = dealer_plays()
        if dealer_count <= 21:
            if player_count == dealer_count:
                print(f"It's a draw!")
            elif player_count < dealer_count:
                print(f"YOU LOST!")
            elif player_count > dealer_count:
                print(f"YOU WON!")
        else:
            print("YOU WON, DEALER BURSTED!")
    else:
        print("YOU LOST DUE TO BURST!")






