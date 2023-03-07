

//Check that the change to STARTED state can just go from pending with the startMeeting() function
rule PendingToStarted(method f, uint256 meetingId) {
   env e;
   calldataarg args;
   uint8 stateBefore = getStateById(e, meetingId);
   f(e, args);
   uint8 stateAfter = getStateById(e, meetingId);

   assert stateAfter == 2 => (stateBefore == 1 || stateBefore == 2) , "Started was created from other state than pending";
   assert (stateBefore == 1 && stateAfter == 2) => f.selector == startMeeting(uint256).selector, "State went from pending to started to other function than startMeeting()";
}

//Number of participants can't be decrease and it can only be increase in the STARTED state
rule numOfParticpants(method f, uint256 meetingId) {
    env e;
    calldataarg args;
    require getStateById(e , meetingId) == 0 => getnumOfParticipants(e, meetingId) == 0;
	uint256 numOfParticipantsBefore = getnumOfParticipants(e, meetingId);
    f(e, args);
    uint256 numOfParticipantsAfter = getnumOfParticipants(e, meetingId);

    assert numOfParticipantsBefore <= numOfParticipantsAfter, "number was decreased";
    assert numOfParticipantsBefore != numOfParticipantsAfter => f.selector == joinMeeting(uint256).selector , "The change of particpants was changed from other function than joinMeeting";

}

//Check that the change to ENDED if enough time has passed and endMeeting() was called
rule StartedToEnd(method f, uint256 meetingId) {
   env e;
   calldataarg args;
   uint8 stateBefore = getStateById(e, meetingId);
   f(e, args);
   uint8 stateAfter = getStateById(e, meetingId);
   uint256 endTimeAfter = getEndTimeById(e , meetingId);

   assert stateAfter == 3 => (stateBefore == 2 || stateBefore == 3) , "ENDED was created from other state than STARTED";
   assert (stateBefore == 2 && stateAfter == 3) => f.selector == endMeeting(uint256).selector, "State went from started to ended to other function than endMeeting()";
   assert (stateBefore == 2 && stateAfter == 3) => endTimeAfter <= e.block.timestamp , "Ended before the end time";
}