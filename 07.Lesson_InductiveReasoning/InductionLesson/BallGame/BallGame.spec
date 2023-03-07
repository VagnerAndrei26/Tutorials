
methods {
	ballAt() returns uint256 envfree
}

invariant neverReachPlayer4() 
	ballAt() != 4 

rule neverReachPlayer4ever(env e) {
	require (ballAt() != 3);
	pass(e);
	assert ballAt() != 4;

}