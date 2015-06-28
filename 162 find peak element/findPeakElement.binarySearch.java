public class Solution {
    public int findPeakHelper(int[] nums, int start, int end) {
        if(start==end) return start;
        int mid=(start+end)/2;
        if(mid<end && nums[mid+1]>nums[mid]) return findPeakHelper(nums, mid+1, end); // In binary search, guard the bound!
        if(mid>start && nums[mid]<nums[mid-1]) return findPeakHelper(nums, start, mid-1);
        return mid;
    }
    public int findPeakElement(int[] nums) {
        int size=nums.length;
        return findPeakHelper(nums, 0, size-1);
    }
}