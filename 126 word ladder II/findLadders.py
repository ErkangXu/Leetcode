class Solution(object):
    charSet=list(string.lowercase)
    def helper(self, word, wl, setList,ind,inp,result):
        if ind==-1:
            result.append(inp)
            return
        for i in xrange(wl):
            for c in self.charSet:
                if c!=word[i]:
                    nw=word[:i]+c+word[i+1:]
                    if nw in setList[ind]:
                        self.helper(nw,wl,setList,ind-1,inp+[nw],result)
                
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordLength=len(beginWord)
        intersection=set()
        frontSetList=[{beginWord}]
        backSetList=[{endWord}]
        midSet=set()
        while True:
            nextSet=set()
            selectList=frontSetList if len(frontSetList[-1])<len(backSetList[-1]) else backSetList
            anotherList=backSetList if len(frontSetList[-1])<len(backSetList[-1]) else frontSetList
            for word in selectList[-1]:
                for i in xrange(wordLength):
                    c=word[i]
                    for z in self.charSet:
                        if z!=c:
                            nc=word[:i]+z+word[i+1:]
                            if nc in wordlist and (len(selectList)==1 or not nc in selectList[-2]):
                                nextSet.add(nc)
            if not nextSet:
                break
            intersection=nextSet.intersection(anotherList[-1])
            if intersection:
                midSet=intersection
                anotherList.pop()
                break
            selectList.append(nextSet)
        result=[]
        for word in midSet:
            frontPortion=[]
            self.helper(word,wordLength,frontSetList,len(frontSetList)-1,[],frontPortion)
            backPortion=[]
            self.helper(word,wordLength,backSetList,len(backSetList)-1,[],backPortion)
            for fCombo in frontPortion:
                for bCombo in backPortion:
                    result.append(fCombo[::-1]+[word]+bCombo)
        return result