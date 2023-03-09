certoraRun Pool.sol:Pool Asset_ERC20.sol SymbolicFlashLoanReceiver.sol \
 --verify Pool:highLevel.spec \
 --link Pool:asset=Asset_ERC20 \
 --send_only \
 --optimistic_loop \
 --msg "Pool Send"