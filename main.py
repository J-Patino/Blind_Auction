from replit import clear
import art
print(art.logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the amount of ${highest_bid}")

while bidding_finished == False:
  name = input("What is your name?")
  price = int(input("What would you like to bid?"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  else:
    print("Type yes or no")

