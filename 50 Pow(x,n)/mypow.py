class Solution:
    def power(self, d, m):
        if m==0:
            return 1
        else:
            v=self.power(d, m//2)  # Need to return integer
            if m%2==0:
                return v*v
            else:
                return v*v*d

    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n<0:
            return 1/self.power(x,-n)
        else:
            return self.power(x,n)
