int firstMissingPositive(int* nums, int numsSize) {
    for(int i=0;i<numsSize;i++) {
        while(nums[i]>0 && nums[i]<=numsSize && nums[i]!=nums[nums[i]-1]) { // The while is the beautiful part
            int tmp=nums[i];
            nums[i]=nums[nums[i]-1];
            nums[tmp-1]=tmp;
        }
    }
    for(int i=0;i<numsSize;i++) if (nums[i]!=i+1) return i+1;
    return numsSize+1;
}