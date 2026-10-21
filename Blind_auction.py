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
    bidder[name] = price # This line adds the elements to the dictionary.
    another_bidder = input("Is there another bidder? (y/n):> ")

winner = max(bidder, key = bidder.get) # This line goes through the keys of the dictionary and compares their values to identify the maximum. The output is the key. 
print(f'The winning bidder is {winner} with the bid of '
      f'${bidder[winner]}!') #Here we get the value assigned to the winner's key.
