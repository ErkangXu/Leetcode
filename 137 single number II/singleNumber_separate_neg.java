public class Solution {
    public int singleNumber(int[] nums) { 
        int max=0;
        int min=0;
        List<Integer> positives = new ArrayList<Integer>();
        List<Integer> negatives = new ArrayList<Integer>();
        for(int i=0; i<nums.length; i++) {
            if (nums[i]>=0) {
                positives.add(nums[i]);
                if (nums[i]>max) max=nums[i];
            } else {
                negatives.add(-nums[i]);
                if (nums[i]<min) min=nums[i];
            }
        }
        int absM;
        int sign=1;
        List<Integer> operativeList;
        if(positives.size()%3==0) {
            absM=-min;
            operativeList=negatives;
            sign=-1;
        } else {
            absM=max; // Get if the single number is negative
            operativeList=positives;
        }
        int bound = Integer.toBinaryString(absM).length(); //toBinaryString()
        int result=0;
        for(int i=0; i<bound; i++) {
            int picker=(1<<i);
            int counter=0;
            for(int n:operativeList) if ((n&picker)!=0) counter++;  // != or == has higher priority that &
            if (counter%3==1) result+=picker;
        }
        return sign*result;
    }           
}