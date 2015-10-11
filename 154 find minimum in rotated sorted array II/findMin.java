public class Solution {
    public int findMinHelper(int[] list, int start, int end) {
        if(list[start]<list[end]) return list[start];
        if(start==end) return list[start];
        if(start+1==end) return Math.min(list[start],list[end]);
        int mid = (start+end)/2;
        if(list[start]<list[mid]) 
            return findMinHelper(list, mid+1, end);
        else if (list[start]>list[mid])
            return findMinHelper(list, start, mid); //Can't use mid-1 here
        else
            return Math.min(findMinHelper(list,mid+1,end),findMinHelper(list,start,mid));
            
    }
    public int findMin(int[] nums) {
        int len = nums.length;
        if(nums.length==1) return nums[0];
        return findMinHelper(nums, 0, len-1); // need to consider when it didn't rotate (includes when there is only one element)
    }
}