/**
 *  * Return an array of arrays of size *returnSize.
 *   * The sizes of the arrays are returned as *columnSizes array.
 *    * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 *     */
void sort(int* input, int start, int end){
    if(start>=end) return;
    int mid=(start+end)/2;
    int mv=input[mid];
    int f=start,b=end;
    while(f<=b){
        while(input[f]<mv) f++;
        while(input[b]>mv) b--;
        if(f<=b) {
            int tmp=input[f];
            input[f++]=input[b];
            input[b--]=tmp;
        }
    }
    sort(input,start,f-1);
    sort(input,f,end);
}
int** subsets(int* nums, int numsSize, int** columnSizes, int* returnSize) {
    int po=1;
    for(int i=1;i<=numsSize;i++) po*=2;
    *returnSize=po;
    *columnSizes=malloc(po * sizeof(int)); // no need to allocate memory for columnSize
    int** result=(int**)malloc(po * sizeof(int*));// The star sign should be put behind int
    (*columnSizes)[0]=0;
    result[0]=(int*)malloc(0);
    if(numsSize==0) return result;
    sort(nums,0,numsSize-1);
    int c=0;
    int p=1;
    for(int i=0;i<numsSize;i++){ // There is no enhanced for loop in C
        int inc=0;
        int ld=nums[i];
        for(int j=0;j<=c;j++){
            int len=(*columnSizes)[j]+1;
            (*columnSizes)[p]=len;
            result[p]=malloc(len*sizeof(int));
            for(int k=0;k<len-1;k++) result[p][k]=result[j][k];
            result[p][len-1]=ld;
            p++;
            inc++;
        }
        c+=inc;
    }
    return result;
}
