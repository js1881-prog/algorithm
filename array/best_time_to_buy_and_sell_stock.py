import sys
from typing import *

sums = [7, 1, 5, 3, 6, 4]

# 브루트 포스
def maxProfitWithBruteForce(self, prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)
    
    return max_price

maxProfitWithBruteForce(Self, sums)
# timeOut으로 문제 해결 불가능


sums = [7, 1, 5, 3, 6, 4]

def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize
    
    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        print("min_price=", min_price)
        profit = max(profit, price - min_price)
        print("profit=", profit)
    
    return profit

maxProfit(Self, sums)
