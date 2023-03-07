

//No fee and owner should be existend if the function ticketDepot() was not called
rule NofeeAndOwner(method f) {
	env e;
	calldataarg args;
	require transactionFee(e) == 0;
	require owner(e) == 0;
	f(e, args);
	uint64 feeAfter = transactionFee(e);
	address ownerAfter = owner(e);

	assert (feeAfter != 0 && ownerAfter != 0) => f.selector == ticketDepot(uint64).selector , "Fee and owner was changed with other function than ticketDepot";
}


// the number of events should never decrease
rule NumOfEventsNeverDecrease(method f) {
	env e;
	calldataarg args;
	uint16 eventsBefore = numEvents(e);
	require f.selector != ticketDepot(uint64).selector;
	f(e,args);
	uint16 eventsAfter = numEvents(e);

	assert eventsBefore <= eventsAfter , "Number of events was decreased";
	assert eventsBefore != eventsAfter => f.selector == createEvent(uint64,uint16).selector, "The number of events was changed from other function then createEvent()";
}

//number of tickets should never increase
rule TicketsShouldNeverIncrease(method f, uint64 ticketPrice, uint16 ticketsAvailable) {
	env e;
	calldataarg args;
	uint16 eventId = createEvent(e,ticketPrice,ticketsAvailable);
	uint16 numberOfTicketsBefore = ticketsRemaining(e, eventId);
	f(e, args);
	uint16 numberOfTicketsAfter = ticketsRemaining(e, eventId);

	assert numberOfTicketsBefore >= numberOfTicketsAfter , "NUmber of tickets was increased" ;
}
