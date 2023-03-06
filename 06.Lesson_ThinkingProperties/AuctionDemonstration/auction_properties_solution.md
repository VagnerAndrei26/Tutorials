Properties for AuctionFixed; 

Properties for token contract :
Unit test:
-Total supply should be >= sum of all balances; ( high level)
-calling the mint function should only increase the balances/totalSupply and decrease them
-transferTo should increase the balanceOf address to all the time, the balance shouldn't decrease or remain the same

Properties of auction contract :
Valid state : 
Auction created : end_time should be greater than 0 / the address of winner should be different than the 0 address so the coin would not be burned
Auction not created : if auction is not created the returns of the getAuction should return all 0 / end_time should be 0

State transitions :
-Prize of the auction cannot be increased
-the bid_time should only be increased and not decrease , every time the bid function is called should increase by 1
-you shouldn't be able to close the bid if the expiry time is == 0 or if block.timestamp is lesser than expiry time or end time;
-if we are in the auction created state and getAuction return only 0 that means that the close function was called and it deleted the specific auction. No other should be able to close an action beside close()