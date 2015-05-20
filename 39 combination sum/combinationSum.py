class Solution:
# @param {integer[]} candidates
# @param {integer} target
# @return {integer[][]}
    result=[] # can't write it as [][]
    length=0

    def addElement(self, lis, target, startIndex, existingElements):
        value=lis[startIndex]
        existingElements.append(value)
        if value==target:
            self.result.append(existingElements)
        else:
            deficit=target-value
            i=startIndex
            while i<self.length:
                value=lis[i]
                if lis[i]<=deficit:
                    newList=list(existingElements)
                    self.addElement(lis,deficit,i,newList)
                else:
                    break
                while i<self.length and lis[i]==value:
                    i+=1

    def combinationSum(self, candidates, target):
        self.result=[] # need to clear the globl variable, because it's filled with the previous test case
        candidates.sort()
        self.length=len(candidates); # must assign to the global name
        i=0
        while i<self.length:
            value=candidates[i]
            if value<=target:
                self.addElement(candidates,target,i,[])
            else:
                break
            while i<self.length and candidates[i]==value: #Need to over come
            the duplication, can use set() on candidates too
            i+=1
            return self.result # member variable need to use self to refer
