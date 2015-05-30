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
            
        rightBound=length-1
        re=target-nums[0]-nums[1]
        if nums[rightBound]>re:
            while nums[rightBound]>re and rightBound>1:
                rightBound-=1
            if rightBound==1:
                rightBound=2
            elif abs(re-nums[rightBound])>abs(re-nums[rightBound+1]):
                rightBound+=1
        re=target-nums[length-1]-nums[length-2]
        leftBound=0
        if nums[leftBound]<re:
            while nums[leftBound]<re and leftBound<length-2:
                leftBound+=1
            if leftBound==length-2:
                leftBound-=1
            elif abs(re-nums[leftBound])>abs(re-nums[leftBound-1]):
                leftBound-=1
                
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
                if remaining==proxy:
                    return target
                diff=abs(remaining-proxy)
                if abs(best-target)>diff:
                    best=existing+proxy
        return best