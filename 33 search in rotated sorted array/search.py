class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start,end=0,len(nums)-1 # Don't forget to minus 1
        while start<end:
            mid=(start+end)/2
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        newList=nums[start:]+nums[:start]
        front,tail=0,len(nums)-1
        while front<=tail:
            mid=(front+tail)/2
            if newList[mid]>target:
                tail=mid-1
            elif newList[mid]<target:
                front=mid+1
            else:
                return (mid+start)%len(nums)
        return -1