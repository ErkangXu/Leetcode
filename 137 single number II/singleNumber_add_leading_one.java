public class Solution {
    public int singleNumber(int[] nums) { 
        int max=nums[0];
        int min=nums[0];
        for(int i=1; i<nums.length; i++) {
            if (nums[i]>max) max=nums[i]; else min=nums[i];
        }
        int absmax=(max>0)? max:-max;
        int absmin=(min>0)? min:-min;
        int absM=(absmax>absmin)? absmax:absmin;
        int bound = Integer.toBinaryString(absM).length(); //toBinaryString()
        int result=0;
        for(int i=0; i<bound; i++) {
            int picker=(1<<i);
            int counter=0;
            for(int n:nums) if ((n&picker)!=0) counter++;  // != or == has higher priority that &
            if (counter%3==1) result+=picker;
        }
        int sign=0;
        int picker=1<<bound;
        int counter=0;
        for(int n:nums) if ((n&picker)!=0) counter++;
        if (counter%3==1) result=result|(-1<<bound);
        return result;
    }           
}