void sortColors(int A[], int n) {
    int i=0;
    int j=n-1;
    while(1){
        while(i<n && A[i]<1) i++; // Need to keep the index in bound
        while(j>-1 && A[j]>=1) j--;
        if (i>j) break; // In the end two pointers will pass by each other, there is no way they stay in the same spot
        int t = A[j];
        A[j]=A[i];
        A[i]=t;
    }
    j=n-1;
    while(i<j){
        while(i<n && A[i]==1) i++; // Used = instead of == in the code originally
        while(j>-1 && A[j]==2) j--;
        if (i>j) break; 
        int t = A[j];
        A[j]=A[i];
        A[i]=t;
    }
}