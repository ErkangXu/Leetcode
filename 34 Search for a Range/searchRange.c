int search(int A[], int s, int e, int target) {
    if (s>e) return -1;
    int m = (s+e)/2; 
    if (A[m]==target) {
        return m;
    }
    else if(A[m]>target) {
        return search(A,s,m-1,target);
    } 
    else {
        return search(A,m+1,e,target);
    }
}

int *searchRange(int A[], int n, int target) {
    int z = search(A,0,n-1,target);
    if (z==-1) {
        int* r=malloc(2*sizeof(int)); // use heap memory is the best way to keep the result right and avoid runtime error
        *r=-1;
        *(r+1)=-1;
        return r;
    } 
    int l=z;
    while((l-1)>=0 && A[l-1]==target){
        l--;
    }
    while((z+1)<n && A[z+1]==target){
        z++;
    }
    int* r=malloc(2*sizeof(int));
    *r=l;
    *(r+1)=z;
    return r;
}