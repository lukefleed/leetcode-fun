class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: buying or selling?
        # If Buy -> i + 1
        # If Sell -> i+2 

        dp = {} # key = (i, buying: bool), val = max_profit

        def dfs(i, buying):
            # base case: if index goes out of bounds
            if i > len(prices):
                return 0
            # base case 2: this pair of values has already computed
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Now we can divide the code in two with an if else statement: if we are buying or if we are selling

            cooldown = dfs(i+1, buying) # max profit, stay in the same state
            if buying:
                # in this state we can buy or cool down
                buy = dfs(i + 1, not buying) - prices[i] # max profit, change the state to selling
                dp[(i, buying)] = max(buy, cooldown) # cache the result
            else: 
                # in this state we can sell or cool down
                sell = dfs(i+2, not buying) + prices[i] # we have to wait 2 days to sell, change the state to buying
                dp[(i, buying)] = max(sell, cooldown) # cache the result

            return dp[(i, buying)]

        return dfs(0, True)
