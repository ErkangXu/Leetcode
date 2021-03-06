class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        stk=[]
        lst=-1
        for i in xrange(len(s)):
            if s[i]=='(':
                if lst!=-1:
                    stk.append(lst)
                else:
                    stk.append(i)
                lst=-1
            else:
                if stk:
                    stt=stk.pop()
                    if i-stt+1>result:
                        result=i-stt+1
                    lst=stt
                else:
                    lst=-1
        return result