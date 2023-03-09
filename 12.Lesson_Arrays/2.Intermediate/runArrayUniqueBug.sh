certoraRun ArrayUniqueSolution.sol:ArrayBugSolution \
--verify ArrayBugSolution:ArrayUniqueBug.spec \
--send_only \
--optimistic_loop \
--loop_iter 4 \
--rule_sanity \
--msg "ArraySolutionBug.sol with sanity check"
