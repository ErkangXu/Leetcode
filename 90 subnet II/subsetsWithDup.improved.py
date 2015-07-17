class Solution:
    list=[]
    result=[]
    length=0
    def subsetsHelper(self,index,subset):
            self.result.append(subset)
            i=index
            while i<self.length:
                newSubset=list(subset)
                val=self.list[i]
                newSubset.append(val)
                self.subsetsHelper(i+1,newSubset)
                while i<self.length and self.list[i]==val:
                    i+=1
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        self.result=[]
        nums.sort()
        self.list=nums
        self.length=len(nums)
        self.subsetsHelper(0,[])
        return self.result