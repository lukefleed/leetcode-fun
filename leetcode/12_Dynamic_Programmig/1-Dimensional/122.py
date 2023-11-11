# dynamic programming approach

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # base case
        if len(prices) == 0:
            return 0

        # initialize the dp array
        dp = [0] * len(prices) # dp[i] represents the max profit at day i

        # fill the dp array
        for i in range(1, len(prices)): # we are choosing the minimum price from the left of the current index
            dp[i] = max(dp[i - 1], dp[i - 1] + prices[i] - prices[i - 1]) # dp[i - 1] + prices[i] - prices[i - 1] is the profit if we sell the stock on day i

        return dp[-1]

# O(n) time complexity, O(n) space complexity

# way more elegant solution (and faster)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

# O(n) time complexity, O(1) space complexity
