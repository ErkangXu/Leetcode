public class Solution {
    public int singleNumber(int[] nums) { 
        int result=0;
        for(int i=0; i<32; i++) {
            int picker=(1<<i);
            int counter=0;
            for(int n:nums) if ((n&picker)!=0) counter++;  // != or == has higher priority that &
            if (counter%3==1) result+=picker;
        }
        return result;
    }           
}