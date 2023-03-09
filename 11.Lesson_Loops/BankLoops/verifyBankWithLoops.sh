certoraRun BankWithLoops.sol:Bank --verify Bank:Loops.spec \
--optimistic_loop \
--loop_iter 2 \
--send_only \
--msg "$1"