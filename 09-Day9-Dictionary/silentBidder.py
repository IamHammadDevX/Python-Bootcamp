import os
print("Welcome to Silent Bidders App")


clear = lambda: os.system("cls")

bids = {}

bidFinished = False

def findHighestBidder(bidRecord):
    highestBid = 0
    winner = ""
    for bidder in bidRecord:
        bidAmount = bidRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestBid}")



while not bidFinished:
    name = input("What is your name? ")
    price = int(input("What is your price? $"))
    bids[name] = price
    shouldContinue = input("Are there any other bidders? type 'yes' or 'no': ")
    clear()
    if shouldContinue == 'no':
        bidFinished = False
        findHighestBidder(bids) 
        break