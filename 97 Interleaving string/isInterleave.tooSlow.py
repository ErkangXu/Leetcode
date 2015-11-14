class Solution(object):
    def helper(self,s1,l1,r1,s2,l2,r2,s3,l3,r3,d):
        if l1>r1:
            return s2[l2:r2+1]==s3[l3:r3+1]
        if l2>r2:
            return s1[l1:r1+1]==s3[l3:r3+1]
        if l3>r3:
            return False
        if d:
            if s1[l1]==s3[l3]:
                if self.helper(s1,l1+1,r1,s2,l2,r2,s3,l3+1,r3,False):
                    return True
            if s2[l2]==s3[l3]:
                if self.helper(s1,l1,r1,s2,l2+1,r2,s3,l3+1,r3,False):
                    return True
        else:
            if s1[r1]==s3[r3]:
                if self.helper(s1,l1,r1-1,s2,l2,r2,s3,l3,r3-1,True):
                    return True
            if s2[r2]==s3[r3]:
                if self.helper(s1,l1,r1,s2,l2,r2-1,s3,l3,r3-1,True):
                    return True
        return False
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self.helper(s1,0,len(s1)-1,s2,0,len(s2)-1,s3,0,len(s3)-1,True)

s=Solution()
s1="cacbbbaaabbacbbbbabbcaccccabaaacacbcaacababbaabbaccacbaabac"
s2="cbcccabbbbaaacbaccbabaabbccbbbabacbaacccbbcaabaabbbcbcbab"
s3="ccbcccacbabbbbbbaaaaabbaaccbabbbbacbcbcbaacccbacabbaccbaaabcacbbcabaabacbbcaacaccbbacaabababaabbbaccbbcacbbacabbaacb"
print(len(s1))
print(len(s2))
print(len(s3))
res=s.isInterleave(s1,s2,s3)
print(str(res))

