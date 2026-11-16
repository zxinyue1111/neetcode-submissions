class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use sliding window to find max profit between buying and selling day
        #find min and max pair that has the largest diff
        #store diff in an array?
        #no profit if array is strictly decreasing

        #[10,1,5,6,7,1]
        minPrice = prices[0]
        maxProfit = 0

        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)
        return maxProfit


            





        


