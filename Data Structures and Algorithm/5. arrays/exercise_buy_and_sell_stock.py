# Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made
# from buying on one day and selling on another.
# In an array of prices, each index represents a day, and the value on that index represents the price of the stocks on that day.

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Solution 1: Brute force
# Complexity: time O(n²), space O(1)
def buy_and_sell_stock_once(prices):
    profit = 0
    for buy in range(len(prices)-1):
        for sell in range(buy+1, len(prices)):
            if prices[sell] - prices[buy] > profit:
                profit = prices[sell] - prices[buy]
            else:
                pass
    return profit

print(buy_and_sell_stock_once(A))


# Solution 2: Tracking min price
# COmplexity: time O(n), space O(1)
def buy_and_sell_stock_once(prices):
    # min_price = prices[0]
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)        
    return max_profit

print(buy_and_sell_stock_once(A))
