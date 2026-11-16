class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use sliding window to find max profit between buying and selling day
        #find min and max pair that has the largest diff
        #store diff in an array?
        #no profit if array is strictly decreasing

        #[10,1,5,6,7,1]
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            sell += 1
        
        return maxProfit


            





        


