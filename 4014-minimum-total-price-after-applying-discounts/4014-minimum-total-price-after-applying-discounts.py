class Solution(object):
    def minPrice(self, prices, discounts):
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        total = 0

        for i in range(min(len(prices), len(discounts))):
            total += prices[i] * (100 - discounts[i])

        for i in range(len(discounts), len(prices)):
            total += prices[i] * 100

        return total / 100.0
        