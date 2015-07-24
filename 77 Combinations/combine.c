/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int len=0;
int x;
int** result;
int* ip;

void pick(int st, int n, int index) {
    if(n>len-st+1) return;
    if(n==0) {
        int* comb=malloc(len*sizeof(int));
        for(int i=0;i<len;i++) comb[i]=ip[i];
        result[x++]=comb;
        return;
    }
    for(int i=st;i<len-n+2;i++){
        ip[index]=i;
        pick(i+1, n-1, index+1);
    }
}

int** combine(int n, int k, int** columnSizes, int* returnSize) {
    if(n==0 || k>n) return NULL;
    len=n;
    int c=1;
    int reduced=(k>n/2)? n-k:k; //if n and k are two big, it might cause c to be inaccurate, use this way to reduce it
    for(int j=n;j>n-reduced;j--) c*=j;
    for(int j=reduced;j>1;j--) c/=j; // Get the return size,
    result = malloc(c*sizeof(int*));
    *columnSizes=malloc(c*sizeof(int));
    for(int i=0;i<c;i++) (*columnSizes)[i]=k;
    *returnSize=c;
    ip=malloc(k*sizeof(int));
    x=0; // It's crucial to reset all the global variables
    pick(1,k,0);
    return result;
}