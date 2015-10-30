class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s:
            if not p:
                return True
            for i in xrange(len(p)):
                if p[i]!='*':
                    return False
        if not p:
            return not s
        if p[0]!='*': # The head and tail have to match
            i=0
            while i<len(p) and i<len(s) and p[i]!='*':
                if p[i]!='?' and p[i]!=s[i]:
                    return False
                i+=1
            if i==len(p):
                return i==len(s)
            if i==len(s): # This part can handle the empty s situation 
                while i<len(p):
                    if p[i]!='*':
                        return False
                    i+=1
        if p[len(p)-1]!='*':
            j=len(p)-1
            k=len(s)-1
            while j>=0 and k>=0 and p[j]!='*':
                if p[j]!='?' and p[j]!=s[k]:
                    return False
                j-=1
                k-=1
        stringList=p.split('*') # This and above logic can handle the no * situation 
        m=0 #This is the starting point for the next search
        for i in xrange(len(stringList)): # the p is * separated words, just need to find all of them in sequence in s
            st=stringList[i]
            if st=='':
                continue # consecutive * can cause empty string in the list
            l=len(st)
            for j in xrange(m,len(s)-l+1): # Find a matching starting point for the selected word
                for k in xrange(l):
                    if st[k]=='?':
                        continue # use continue here instead of put "st[k]!='?'" in the next clause maks code faster(lots of ?)
                    if st[k]!=s[j+k]:
                        break
                else: # Means found a match(no break from for loop)
                    m=j+l # Need to update m for the next search
                    break
            else: # Means didn't find a match in s
                return False        
        return True # Found all the words in s
                