class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        writeIndex=0
        probeIndex=0
        while probeIndex<len(nums):
            currentValue=nums[probeIndex]
            couter=0
            while probeIndex<len(nums) and nums[probeIndex]==currentValue:
                couter+=1
                probeIndex+=1
            nums[writeIndex]=currentValue
            writeIndex+=1
            if couter>=2:
                nums[writeIndex]=currentValue # At most repeat once, no need for a loop structure
                writeIndex+=1
        return writeIndex