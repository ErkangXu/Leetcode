class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        le=len(prices)
        if le<2:
            return 0
        min=prices[0]
        fp=[0 for i in xrange(le)] # at the same index, profit is 0, appending or inserting to list is very expensive!
        for i in xrange(1,le):
            if prices[i]<min:
                min=prices[i]
            if prices[i]-min>fp[i-1]:
                fp[i]=prices[i]-min
            else:
                fp[i]=fp[i-1]
        max=prices[le-1]
        bp=[0 for i in xrange(le) ]
        for i in xrange(le-2,-1,-1):
            if prices[i]>max:
                max=prices[i]
            if max-prices[i]>bp[i+1]:
                bp[i]=max-prices[i]
            else:
                bp[i]=bp[i+1]
        maxP=0
        for i in xrange(le):
            if fp[i]+bp[i]>maxP:
                maxP=fp[i]+bp[i]
        return maxP
        