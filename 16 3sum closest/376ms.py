class Solution:
    def findClosest(self, nums, start, end, target):
        if target<=nums[start]:
            return start
        elif target>=nums[end]:
            return end
        else:
            mid=(start+end)/2
            midV=nums[mid]
            if midV>target:
                leftClosest=self.findClosest(nums,start,mid-1,target)
                if leftClosest==mid-1 and abs(nums[leftClosest]-target)>abs(nums[mid]-target):
                    return mid
                else:
                    return leftClosest
            elif midV<target:
                rightClosest=self.findClosest(nums,mid+1,end,target)
                if rightClosest==mid+1 and abs(nums[rightClosest]-target)>abs(nums[mid]-target):
                    return mid
                else:
                    return rightClosest
            else:
                return mid
                
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
            
        rightBound=self.findClosest(nums,2,length-1, target-nums[0]-nums[1])
        leftBound=self.findClosest(nums,0,length-3, target-nums[length-1]-nums[length-2])
        dic={}
        dic[nums[leftBound]]=nums[leftBound]
        for i in xrange(leftBound+1,rightBound+1):
            mid=(nums[i-1]+nums[i])/2
            for j in xrange(nums[i-1]+1,mid+1):
                dic[j]=nums[i-1]
            for k in xrange(mid+1,nums[i]+1):
                dic[k]=nums[i]
                
        
        best=firstThree
        for i in xrange(leftBound,rightBound-1):
            for j in xrange(i+1,rightBound):
                existing=nums[i]+nums[j]
                remaining=target-existing
                proxy=0
                if remaining>nums[rightBound]:
                    proxy=nums[rightBound]
                elif remaining<nums[j+1]:
                    proxy=nums[j+1]
                else:
                    proxy=dic[remaining]
                diff=abs(remaining-proxy)
                if abs(best-target)>diff:
                    best=existing+proxy
        return best
        