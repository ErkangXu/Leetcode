public class Solution {
    public int maxSubArray(int[] nums) {
        int len =nums.length;
        if(len==1) return nums[0]; // Handles the situation where the array has only one element
        int[] inc = new int[len];
        inc[0]=nums[0];
        int max=0;
        int min=0;
        int minb=0;
        for(int i=1;i<len;i++){
            inc[i]=inc[i-1]+nums[i];
            if(inc[i]>=inc[max]) {
                max=i;
                minb=min;
            } else if(inc[i]<inc[min]) min=i;
        }
        int fsum = (inc[minb]>0 || minb==max)? inc[max] : inc[max]-inc[minb]; // If the lowest point is larger that 0, or only one element
        if(min<=max) return fsum;
        int esum = maxSubArray(Arrays.copyOfRange(nums,max+1,len)); // The element of end parameter is no included in the copied array 
        return (fsum>esum)? fsum:esum;
    }
}