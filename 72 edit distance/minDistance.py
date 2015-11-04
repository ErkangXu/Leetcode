class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lst=[i for i in xrange(len(word2)+1)]
        for i in xrange(1,len(word1)+1):
            prev=i # The edit distance to delete to empty string
            for j in xrange(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    cur=lst[j-1]
                else:
                    cur=min( min(prev,lst[j]), lst[j-1])+1
                lst[j-1]=prev
                prev=cur
            lst[len(word2)]=prev
        return lst[len(word2)]