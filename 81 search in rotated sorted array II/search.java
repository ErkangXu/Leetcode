public class Solution {
    int tar;
    public boolean searchHelper(int[] nums, int start, int end) {
        if(start>end) return false;
        if(start==end) return tar==nums[start];
        if (tar==nums[start] || tar==nums[end]) return true;
        int mid=(start+end)/2;
        if (tar==nums[mid]) return true;
        if(nums[start]<nums[mid]) {
            if(tar>nums[start] && tar<nums[mid]) return searchHelper(nums,start+1,mid-1);
            return searchHelper(nums,mid+1,end-1);          
        } else if(nums[start]>nums[mid]){
            if(tar>nums[mid] && tar<nums[end]) return searchHelper(nums,mid+1,end-1); 
            return searchHelper(nums,start+1,mid-1);
        } else return searchHelper(nums,mid+1,end-1) || searchHelper(nums,start+1,mid-1);  //[1,1,3,1] or [1,3,1,1,1]   
    }
    public boolean search(int[] nums, int target) {
        tar=target;
        return searchHelper(nums, 0, nums.length-1);
    }
}