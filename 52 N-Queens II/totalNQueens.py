class Solution(object):
    count=0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count=0
        self.helper(n,set(),set(),set(),0)
        return self.count
    def helper(self,d,cSet,pSet,mSet,ind):
        print('ind is:'+str(ind))
        if ind==d:
            self.count+=1
            return
        for c in xrange(d):
            print('    c is:'+str(c))
            if not c in cSet and not (ind+c) in pSet and not (ind-c) in mSet:
                self.helper(d,cSet|{c},pSet|{ind+c},mSet|{ind-c},ind+1)
