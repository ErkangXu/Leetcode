class Solution:
    result=[]
    extent=0
    
    def subsetsHelper(self,keys,freqs,index,li):
        nl=li
        for j in xrange(0,freqs[index]):
            nl=list(nl)
            nl.append(keys[index])
            self.result.append(nl)
            for i in xrange(index+1,self.extent):
                nextList=list(nl)
                self.subsetsHelper(keys,freqs,i,nextList)
            
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        self.result=[]
        extent=0
        nums.sort()
        keys=[]
        freqs=[]
        chang=len(nums)
        i=0
        while i < len(nums):
            val=nums[i]
            j=i
            while(j<chang and nums[j]==val):
                j+=1
            keys.append(val)
            freqs.append(j-i)
            i=j
        self.extent=len(keys)
        self.result.append([])
        for i in xrange(0,self.extent):
            self.subsetsHelper(keys,freqs,i,[])
        return self.result