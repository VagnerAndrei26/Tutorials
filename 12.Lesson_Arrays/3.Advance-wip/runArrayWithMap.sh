certoraRun ArrayWithMap.sol \
--verify ArrayWithMap:ArrayWithMap.spec \
--send_only \
--optimistic_loop \
--loop_iter 4 \
--rule_sanity \
--msg "ArrayWithMap.sol with sanity check"