class Solution(object):
    def helper(self, s, sl, si, wordDict, lenSet, lis, res):
        if si==sl:
            res.append(' '.join(lis))
            return
        for l in lenSet:
            if sl-si>=l and s[si:si+l] in wordDict: #Shouls be >= herr
                self.helper(s,sl,si+l,wordDict,lenSet,lis+[s[si:si+l]],res)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not s:
            return []
        result=[]
        lengthSet=set()
        dicCharset=set()
        minLen=len(s)
        for word in wordDict:
            if len(word)<minLen:
                minLen=len(word)
            lengthSet.add(len(word))
            for char in word:
                dicCharset.add(char)
        stringCharset=set()
        for char in s:
            stringCharset.add(char)
        if stringCharset-dicCharset:
            return []
        for l in lengthSet:
            if s[-l:] in wordDict:
                break 
        else:
            return [] # There should be a way to finish the s with a word in the dict, if not return empty list
        self.helper(s, len(s), 0, wordDict, lengthSet, [], result)
        return result