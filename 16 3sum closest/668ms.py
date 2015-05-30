class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        length=len(nums)
        nums.sort()
        firstThree=nums[0]+nums[1]+nums[2]
        if target<firstThree:
            return firstThree
        lastThree=nums[length-1]+nums[length-2]+nums[length-3]
        if target>lastThree:
            return lastThree
        dic={}
        dic[nums[0]]=nums[0]
        for i in xrange(1,length):
            mid=(nums[i-1]+nums[i])/2
            for j in xrange(nums[i-1]+1,mid+1):
                dic[j]=nums[i-1]
            for k in xrange(mid+1,nums[i]+1):
                dic[k]=nums[i]
        
        best=firstThree
        for i in xrange(0,length-2):
            for j in xrange(i+1,length-1):
                existing=nums[i]+nums[j]
                remaining=target-existing
                proxy=0
                if remaining>nums[length-1]:
                    proxy=nums[length-1]
                elif remaining<nums[j+1]:
                    proxy=nums[j+1]
                else:
                    proxy=dic[remaining]
                diff=abs(remaining-proxy)
                if abs(best-target)>diff:
                    best=existing+proxy
        return best