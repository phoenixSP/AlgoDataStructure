# 🟡 Coin Change

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return _the fewest number of coins that you need to make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Solution
        - Lets look at a bottom up approach and calculate the number of coins needed for all values from 0 - amount
        - At each value, the amount can be made by the following: amount = coin_i + dp[amount - coin_i]
        - amount 0 can be made by 0 coins
        - keep iterating on dp indices and coin indices

        TC: O(amount*len(coins))
        SC: O(amount)
        '''
        if not coins or len(coins) == 0:
            return 0 
        
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1,  dp[i]) # + 1 for the new coin
        
        return dp[amount] if dp[amount] != float('inf') else -1
```
