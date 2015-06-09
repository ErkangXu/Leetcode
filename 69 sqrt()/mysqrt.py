class Solution:
    def sqrtHelper(self,x):
        if x<4:
            return 1
        else:
            return 2*self.sqrtHelper(x//4)
            
    def findAccurate(self,s,e,t):
        if s>e:
            return e
        mid=(s+e)/2
        if mid**2==t:
            return mid
        elif mid**2<t:
            return self.findAccurate(mid+1,e,t)
        else:
            return self.findAccurate(s,mid-1,t)
            
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x==0:
            return 0
        elif x<4:
            return 1
        estimate=self.sqrtHelper(x)
        rightB=estimate*2 if estimate<x else x
        return self.findAccurate(estimate, rightB, x)