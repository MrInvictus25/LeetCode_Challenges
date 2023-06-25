# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
# return 0.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = None
        maximum_profit = 0  # Keeping track of the largest difference
        for price in prices:
            if min_price is None:
                min_price = price
            elif price < min_price:
                min_price = price
            elif price - min_price > maximum_profit:
                maximum_profit = price - min_price

        return maximum_profit

example = Solution()
print(example.maxProfit([7, 1, 5, 3, 6, 4]))


class Solution1:
    def maxProfit(self, prices: list[int]) -> int:
        maximum_profit = 0  # Keeping track of the largest difference
        for purchaseDay in range(len(prices) - 1):  # Iteration through every day in prices. -1 means that we do not need the last digit
            for vendDay in range(purchaseDay + 1, len(prices)):  # Iteration through every day after purchaseDay
                #print(vendDay)
                #print(lst[vendDay])
                transaction = prices[vendDay] - prices[purchaseDay]
                if transaction > maximum_profit:
                    maximum_profit = transaction
        return maximum_profit

example = Solution1()
print(example.maxProfit([7, 1, 5, 3, 6, 4]))




