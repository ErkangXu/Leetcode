class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result=[]
        if len(s)==0 or len(words)==0:
            return result
        wL=len(words[0])
        lL=len(words)
        dic={}
        for w in words:
            dic[w]=dic[w]+1 if w in dic else 1
        for i in xrange(wL):
            print('i')
            print(i)
            left,cnt=i,0
            iDic={}
            for j in xrange(i,len(s)-wL+1,wL):
                print('j')
                print(j)
                wd=s[j:j+wL]
                print("wd is:" + wd)
                if wd in dic:
                    iDic[wd]=iDic[wd]+1 if wd in iDic else 1
                    cnt+=1
                    while iDic[wd]>dic[wd]:
                        awd=s[left:left+wL]
                        if iDic[awd]>1:
                            iDic[awd]=iDic[awd]-1
                        else:
                            del iDic[awd]
                        cnt-=1
                        left+=wL
                    print("cnt is:"+str(cnt))
                    if cnt==lL:
                        result.append(left)
                        awd=s[left:left+wL]
                        if iDic[awd]>1:
                            iDic[awd]=iDic[awd]-1
                        else:
                            del iDic[awd]
                        cnt-=1
                        left+=wL
                else:
                    iDic={}
                    cnt=0
                    left=j+wL
        return result