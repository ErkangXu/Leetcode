ass Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        min=prices[0]
        maxP=0
        for i in xrange(1,len(prices)):
            if prices[i]<min:
                min=prices[i]
            elif prices[i]-min>maxP:
                maxP=prices[i]-min
        return maxP
