class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        front, back=set([beginWord]), set([endWord]) # Must use set to make the search faster
        length=2
        width=len(beginWord)
        charSet=list(string.lowercase)
        wordDict.discard(beginWord)
        wordDict.discard(endWord)
        while front:
            newFront=set()
            for phrase in front:
                for i in xrange(width):
                    for c in charSet:
                        nw=phrase[:i]+c+phrase[i+1:]
                        if nw in back:
                            return length
                        if nw in wordDict:
                            newFront.add(nw)
            front=newFront
            if len(front)>len(back):
                front,back=back,front
            wordDict-=front
            length+=1
        return 0