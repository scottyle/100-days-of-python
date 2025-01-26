import art
print(art.logo)

auction_over = False
auction_dict = {}
highest_bid = 0
highest_bidder_name = ""
# TODO-1: Ask the user for input
while not auction_over:
    auction_name = input("What is your name?: ")
    auction_price = int(input("What is your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': \n")
    print("\n" * 100)
    # TODO-2: Save data into dictionary {name: price}
    auction_dict[auction_name] = auction_price
    if other_bidders == 'no':
        auction_over = True
        print(auction_dict)

for bids in auction_dict:
    if auction_dict[bids] > highest_bid:
        highest_bid = auction_dict[bids]
        highest_bidder_name = bids

print(f"The winner is {highest_bidder_name} with a bid of ${highest_bid}")
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


