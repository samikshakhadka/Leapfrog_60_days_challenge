#Best time to buy and sell stock
# Given an array of prices of length N, representing the price of sticks on different days,
# the task is to find the max profit possible for buying and selling stocks
#on different days using transactions 
#only one transaction is allowed and
#stock must be brought before being sold

def maxprofit(prices, n):
    buy = prices[0]
    max_profit = 0

    for i in range (1,n):
        if (buy > prices[i]):
            buy = prices[i]

        elif ( prices[i] - buy > max_profit):
            max_profit = prices[i] - buy
    return max_profit

if __name__ == '__main__':

    prices = [7,2,4,6,8,3,8]
    n = len(prices)
    maxprofit = maxprofit(prices, n)
    print(maxprofit)
    