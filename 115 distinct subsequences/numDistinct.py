class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m=[ [0 for j in xrange(len(s)+1)] for i in xrange(len(t)+1)]
        for j in xrange(len(s)):
            m[0][j]=1
        for i in xrange(1,len(t)+1):
            for j in xrange(i,len(s)+1): # if the length of t is bigger the length of s, the numbers of susequence is 0 for sure, no need to loop though them
                if t[i-1]==s[j-1]:
                    m[i][j]=m[i][j-1]+m[i-1][j-1]
                else:
                    m[i][j]=m[i][j-1]
        return m[len(t)][len(s)]