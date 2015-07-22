class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        result=[] 
        result.append(0)
        for i in xrange(n):
            pow=2**i
            j=pow-1
            while j>=0:
                result.append(result[j]+pow)
                j-=1
        return result # if n=0 should return [0]