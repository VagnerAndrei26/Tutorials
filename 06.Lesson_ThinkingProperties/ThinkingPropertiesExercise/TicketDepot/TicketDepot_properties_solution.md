# Properties for TicketDepot

States of the contract:
```ruby
- `noSeller` - (no seller initiated/fees == 0) no seller used the ticketDepot function
- `Seller` - (seller initiated contract> fees > 0) there is an owner of the contract that initiated the ticketDepot function
```

1. ***Valid state*** - `noSeller` => transactionFee should be 0 and owner should be the 0 address;
2. ***Valid state*** - `Seller` => transactionFee should be greater than 0 and the owner should be the tx.origin caller of the ticketDepot()
3. ***Variable transition*** - the numEvents variable should never decrease, it should only increase as the number
4. ***Variable transition*** -  the number of ticketsRemaining should never increase after an event was created
5. ***Variable transition*** - the attendees should only be changes from the buyOfferedTicket() and buyNewTicket() functions
6. ***High-level*** - the number of events should only be changed by createEvent() function
7. ***Unit tests*** - buyNewTicket() should set the attendee correctly
8. ***Unit tests*** - buyOfferedTicket() should change the attendee correctly

## Prioritizing

### High Priority:
- 2 if the fee is 0 or the owner is someone else the seller would not benefit from it
- 4 if someone can increase the number of ticketsRemaining then it can create an infinite amount of tickets to an event
- 5 if you can change the attendees from other functions without paying then people can steal the tickets
- 3 if you can decrease the number of events you can make some duplicate some events and change their values

### Medium Priority:
- 1 see that the state is set correctly

### Low Priority:
6,7,8 are low priority since they check the implementation of some specific functions
