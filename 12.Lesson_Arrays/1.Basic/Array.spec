// #contract Array.sol:Array
methods {
    get(uint) returns (address) envfree
    getWithDefaultValue(uint) returns (address) envfree
}



invariant uniqueArraySolution(uint256 i, uint256 j)
    i != j => (
        (getWithDefaultValue(i) != getWithDefaultValue(j)) || 
		((getWithDefaultValue(i) == 0) && (getWithDefaultValue(j) == 0))
	)

invariant inArrayIsListed(uint256 i)
	(i < getLength()) => isListed(getWithDefaultValue(i))