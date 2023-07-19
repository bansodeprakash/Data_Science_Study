
#HINT: You can call clear() to clear the output in the console.
def maximum_bid(bid_highest):
  maximum = 0
  
  for greater in bid_highest:
      bid_price = bid_highest[greater]
      if bid_price > maximum:
        maximum = bid_price  
  print(f"winner is {greater} bid of ${maximum}")  
      
empty_bid = { }
end_auction = False
while not end_auction:
  
  bid_name = str(input("what is your name? "))
  bid_value = int(input("what is your bid ?  $"))
  
  empty_bid [bid_name] = bid_value
  other_bid = input("type 'yes' for other bidders or type 'no' ")
  
  if other_bid == 'no':
   end_auction = True  
   
maximum_bid(empty_bid)  
