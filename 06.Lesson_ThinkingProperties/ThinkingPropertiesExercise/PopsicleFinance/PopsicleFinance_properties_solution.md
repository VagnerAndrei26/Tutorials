# Properties for popsicleFinance

States of the contract:
```ruby
- `noDeposit` - (no deposit/fees == 0)no feed to be distributed because the owner job was not done
- `Deposit` - (fees> 0) fees are bigger than 0 and
```

1. ***Valid state*** - `noDeposit` => totalFeesEarnedPerShare should always be 0
2. ***Valid state*** - `Deposit` => totalFeesEarnedPerShare should be bigger than 0 so people can collect fees per shares after they deposit
3. ***Variable transition*** -`Deposit` => rewards cannot decrease beside calling the function collectFees()
4. ***Variable transition*** -`Deposit` => rewards cannot increase beside calling the function deposit() or withdraw()
5. ***High-level*** - No way to gain more Lp tokens beside calling deposit() which calls mint()
6. ***High-level*** - No way to lose  Lp tokens beside calling withdraw() which calls burn()
7. ***High-level*** - totalSupply should be >=  than the balances of all the users lp tokens
8. ***High-level*** - rewards are correctly for deposit() and withdraw()

## Prioritizing

### High Priority:
4/5 because you can change the rewards of the share holders
3/6 because people can lose rewards
8 the rewards are correct and can't be changed so people will not lose/gain more rewards

### Medium Priority:
6 system has enough tokens for people to withdraw()/burn()
 
### Low Priority:
1/2 changes the state of the contract, if fees are 0, people can just deposit() and withdraw() without losing/gaining anything