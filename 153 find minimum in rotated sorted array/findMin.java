public class Solution {
    public int findMinHelper(int[] list, int start, int end) {
        if(list[start]<=list[end]) return list[start];
        int mid = (start+end)/2;
        if(list[start]<=list[mid]) {
            return findMinHelper(list, mid+1, end);
        } else return findMinHelper(list, start, mid);
    }
    public int findMin(int[] nums) {
        int len = nums.length;
        return findMinHelper(nums, 0, len-1); // need to consider when it didn't rotate (includes when there is only one element)
    }
}