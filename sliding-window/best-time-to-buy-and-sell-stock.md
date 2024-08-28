# 🟢 Best Time to Buy and Sell Stock

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

{% code overflow="wrap" %}
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    '''
    Brute force:
    Iterate i and j over the array, calculate profit and return the max
    for i in range(0, n - 1):
    for j in range(i+1, n):
    
    TC: O(n^2), SC: O(1)
    
    Solution:
    Approach this as a sliding window/two-pointer problem where left is updated 
    when equal to/smaller than right
    
    TC: O(n), SC: O(1)
    '''
        if prices is None or len(prices) == 0:
            return 0

        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):

            buy = prices[left]
            sell = prices[right]

            if buy < sell:
                profit = sell - buy
                max_profit = max(max_profit, profit)

                right += 1
            else:
                left = right
                right = left + 1

        return max_profit
```
{% endcode %}

It can be slightly optimized by reducing number of lines, but overall time complexity remains the same

{% code overflow="wrap" %}
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0

        max_profit = 0
        lowest = prices[0]

        for price in prices[1:]:
            if price < lowest:
                lowest = price
            # if current is lowest, then curr profit = 0, which does not affect max_profit 
            max_profit = max(max_profit, price - lowest)

        return max_profit 
```
{% endcode %}
