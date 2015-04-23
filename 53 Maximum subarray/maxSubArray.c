int maxSubArrayHelper(int* nums, int start, int end){
    if(start==end) return nums[start];
    if(end==start+1) { // used = instead of = at first
        int s=nums[start], e=nums[end];
        if(s>=0 && e>=0) return s+e;
        return (s>e)? s:e;
    }
    int mid=(start+end)/2;
    int lm = maxSubArrayHelper(nums,start,mid);
    int rm = maxSubArrayHelper(nums,mid+1,end);
    int sum=0,lr=INT_MIN;
    for(int i=mid;i>=start;i--){
        sum+=nums[i];
        if(sum>lr) lr=sum;
    }
    sum=0; int rl=INT_MIN;
    for(int i=mid+1;i<=end;i++){
        sum+=nums[i];
        if(sum>rl) rl=sum;
    }
    int mv = (lm>rm)? lm:rm;
    if(mv<lr+rl) mv=lr+rl;
    return mv;
}
int maxSubArray(int* nums, int numsSize) {
    return maxSubArrayHelper(nums, 0, numsSize-1);
}