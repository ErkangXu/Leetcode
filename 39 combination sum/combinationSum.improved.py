class Solution:
    list=[]
    result=[] # can't write it as [][]
    length=0
    def sumHelper(self, startIndex, target, solution):
        i=startIndex
        while i<self.length:
            value=self.list[i]
            if value<target:
                updatedSolution=list(solution)
                updatedSolution.append(value)
                self.sumHelper(i,target-value,updatedSolution)
            elif value==target:
                solution.append(value)
                self.result.append(solution)
                return
            else:
                break
            while i<self.length and self.list[i]==value: #Need to over come the duplication, can use set() on candidates too, but it might has too much duplications
                i+=1
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}               
    def combinationSum(self, candidates, target):
        self.result=[] # need to clear the globl variable, because it's filled with the previous test case
        candidates.sort()
        self.list=candidates
        self.length=len(candidates); # must assign to the global name
        self.sumHelper(0,target,[])
        return self.result # member variable need to use self to refer