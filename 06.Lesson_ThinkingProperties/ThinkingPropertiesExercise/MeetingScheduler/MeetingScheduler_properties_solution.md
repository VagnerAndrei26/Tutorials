# Properties for meetingScheduler

States of the contract : 
```Ruby
- "UNINITIALIZED" - (Not created) is defined as ScheduledMeeting[id].endTime == 0 &&  ScheduledMeeting[id].startTime == 0 && ScheduledMeeting[id].numOfParticipants == 0 && ScheduledMeeting[id].organizer == 0 && ScheduledMeeting[id].status == 0
- "PENDING" - (created and in pending) is defined as ScheduledMeeting[id].endTime =! 0 &&  ScheduledMeeting[id].startTime =! 0 && ScheduledMeeting[id].startTime < ScheduledMeeting[id].endTime && ScheduledMeeting[id].numOfParticipants == 0 && ScheduledMeeting[id].status == 1
- "STARTED" - (created and started) is defined as ScheduledMeeting[id].endTime =! 0 &&  ScheduledMeeting[id].startTime =! 0 && ScheduledMeeting[id].startTime < ScheduledMeeting[id].endTime && ScheduledMeeting[id].status == 2
- "ENDED" - (created started and ended) is defined as ScheduledMeeting[id].endTime =! 0 &&  ScheduledMeeting[id].startTime =! 0 && ScheduledMeeting[id].startTime < ScheduledMeeting[id].endTime &&  ScheduledMeeting[id].status == 3
- "CANCELLED" - (created, in pending and cancelled) is defined as ScheduledMeeting[id].endTime =! 0 &&  ScheduledMeeting[id].startTime =! 0 && ScheduledMeeting[id].startTime < ScheduledMeeting[id].endTime && ScheduledMeeting[id].status == 4
```

1. ***VALID STATE*** - "UNINITIALIZED" => getStateById(id) should return 0 / getStartTimeById(id) should return 0 / getEndTimeById(id) should return 0 / getnumOfParticipants(id) should return 0
2. ***VALID STATE*** - "PENDING" => getStartTimeById(id) should be lesser than getEndTimeById(id), ScheduledMeeting[id].organizer should be the caller of the scheduleMeeting function,
ScheduledMeeting[id].numOfParticipants should be equal to 0; 
3. ***VALID STATE*** - "STARTED" => Should only change from PENDING state, only the owner of the pending can cancel the changing it to CANCELLED
4. ***VALID STATE*** - "ENDED" => if ScheduledMeeting[id] is in STARTED state and block.timestamp is > ScheduledMeeting[id].endTime
5. ***VALID STATE*** - "CANCELLED" => only the owner of the pending can cancel the changing it to CANCELLED, if block.timestamp > ScheduledMeeting[id].endTime it can't be set to cancelled
6.***Variable transition*** - Number of participants can't decreased and also it can be increased only in the STARTED state
7.***High-level*** - Only the organizer of a meeting should be able to CANCEL a meeting from the PENDING state
8.***Unit tests*** - scheduleMeeting() should not let starTime be greater than endTime
9.***Unit tests*** - startMeeting() should change the state correctly and should only be called from the PENDING state
10.***Unit tests*** - cancelMeeting() should change the state correctly and only be called by the owner in the PENDING STATE, can't cancel an ENDED state meeting
11.***Unit tests*** - endMeeting() should change the state correctly and only be from the STARTED state after block.timestamp is greater than endTime

## Prioritizing

### High Priority:

4 , 5 are high priority because it can change the state to ENDED or CANCELLED without the approve of the owner or block.timestamp being bigger than endTime
6 is important because the number of participants shouldn't decrease in any situation

### Low Priority:
Rest are low priority
