logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bidder = {}
another_bidder = 'y'
while another_bidder == 'y':
    print("\n" * 200)
    print(logo)
    name = input("What is your name?: ")
    price = int(input("What's your bid: $"))
    while price in bidder.values():
        print("Your bid is not unique. Please, try something else.")
        price = int(input("What's your bid: $"))
    bidder[name] = price # This line adds the elements to the dictionary.
    another_bidder = input("Is there another bidder? (y/n):> ")

winner = max(bidder, key = bidder.get) # This line goes through the keys of the dictionary and compares their values to identify the maximum. The output is the key. 
print(f'The winning bidder is {winner} with the bid of '
      f'${bidder[winner]}!') #Here we get the value assigned to the winner's key.

#Second version of the same program without using max()
bidder = {}
highest_bid = 0
winner = ""
another_bidder = 'y'
while another_bidder == 'y':
    print("\n" * 200)
    print(logo)
    name = input("What is your name?: ")
    price = int(input("What's your bid: $"))
    while price in bidder.values():
        print(f"Your bid is not unique. Try something else!")
        price = int(input("What's your bid: $"))
    bidder[name] = price
    another_bidder = input("Is there another bidder? (y/n): ")
for name in bidder:
    price = bidder[name]
    if price > highest_bid:
        highest_bid = price
        winner = name
print(f'The winner of the auction is {winner} with the bid of ${bidder[winner]}')
