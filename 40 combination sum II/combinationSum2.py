class Solution:
    list=[]
    result=[]
    length=0
    def sumHelper(self,start,target,solution):
        for i in xrange(start, self.length):
            val=self.list[i]
            if i!=start and val==self.list[i-1]:
                continue  # at the same level, the same number should be counted once, by doing this we don't need a freq list
            if val<target:
                newlist=list(solution)
                newlist.append(val)
                self.sumHelper(i+1,target-val,newlist)
            elif val==target:
                solution.append(self.list[i])
                self.result.append(solution)
                return
            else:
                break
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        self.result=[]
        candidates.sort() # the sort method doesn't return, it sorts the calling list only
        self.list=candidates
        self.length=len(candidates)
        self.sumHelper(0,target,[])
        return self.result