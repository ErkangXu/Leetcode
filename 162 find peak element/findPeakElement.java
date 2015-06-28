public class Solution {
    public int findPeakElement(int[] nums) {
        int size=nums.length;
        if(size==1) return 0; // Should return the index, not the element
        int p=0;
        while(p<size-1 && nums[p]>nums[p+1]) p++;
        if(p==size-1) return 0; // Wrote == as = at first
        while(p<size-1 && nums[p]<nums[p+1]) p++;
        return p;
    }
}