class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        lreach=0
        reach=nums[0]
        jump=1
        while reach<len(nums)-1:
            nreach=reach
            for i in xrange(lreach+1,reach+1):
                if i+nums[i]>len(nums)-2:
                    return jump+1
                if i+nums[i]>nreach:
                    nreach=i+nums[i]
            lreach=reach
            reach=nreach
            jump+=1
        return jump