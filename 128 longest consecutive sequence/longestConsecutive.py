class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        i=1
        result=1
        while i < len(nums):
            count=1
            while i<len(nums) and ( nums[i]==nums[i-1]+1 or nums[i]==nums[i-1]):
                if nums[i]==nums[i-1]+1:
                    count+=1
                i+=1
            if count>result:
                result=count
            i+=1
        return result