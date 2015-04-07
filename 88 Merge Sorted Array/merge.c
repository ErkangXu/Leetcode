/*
void merge(int A[], int m, int B[], int n) {
    if(m==0) {
        for(int i=0;i<n;i++) A[i]=B[i];
        return;
    }
    for(int i=m-1;i>-1;i--){
        A[i+n]=A[i];
    }
    int p=n,q=0,x=0;
    while(q<n && p<m+n){
        if(A[p]<B[q]) {
            A[x++]=A[p++];
        }else {
            A[x++]=B[q++];
        }
    }
    if(q==n) {
        while(p<m+n) A[x++]=A[p++];
    } else {
        while(q<n) A[x++]=B[q++];
    }
}
*/ // There is no need to move elements in A to the tail, we can merge from the back

void merge(int A[], int m, int B[], int n) {
    int x=m+n-1;
    int p=m-1;
    int q=n-1;
    while(p>-1 && q>-1) {
        if(A[p]>B[q]) {
            A[x--]=A[p--];
        } else A[x--]=B[q--];
    }
    while(q>-1) A[x--]=B[q--];
}