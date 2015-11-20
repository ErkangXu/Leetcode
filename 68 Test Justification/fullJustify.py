class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []
        result=[]
        i=0
        while True:
            initLen=len(words[i])
            line=words[i]
            i+=1
            start=i
            while i<len(words) and initLen<maxWidth:
                initLen+=len(words[i])+1
                i+=1
            if initLen>maxWidth:
                i-=1
                initLen-=len(words[i])+1
            if i==len(words):
                for j in xrange(start,i):
                    line+=' '+words[j]
                line+=' '*(maxWidth-initLen)
                result.append(line)
                return result
            if start==i:
                line+=(maxWidth-initLen)*' '
            else:
                paddingL=maxWidth-initLen
                basePadLen=paddingL/(i-start)+1
                extraPadNum=paddingL%(i-start)
                for j in xrange(start,start+extraPadNum):
                    line+=(basePadLen+1)*' '+words[j]
                for j in xrange(start+extraPadNum,i):
                    line+=basePadLen*' '+words[j]
            result.append(line)