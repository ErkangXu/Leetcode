class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        result=[[0 for x in range(n)] for x in range(n)] 
        iteN=(n+1)/2
        currentN=1
        for i in xrange(iteN):
            upB=i
            downB=n-1-i
            leftB=i
            rightB=n-1-i
            for j in xrange(leftB,rightB+1):
                result[upB][j]=currentN;
                currentN+=1
            for j in xrange(upB+1,downB+1):
                result[j][rightB]=currentN;
                currentN+=1
            #if upB!=downB: # There is no need for this, because if upB==downB rightB would == leftB, the loop won't run already
            for j in xrange(rightB-1,leftB-1,-1):
                result[downB][j]=currentN
                currentN+=1
            #if leftB!=rightB:
            for j in xrange(downB-1,upB,-1):
                result[j][leftB]=currentN
                currentN+=1
        return result