int numTrees(int n) {
    if(n==0 || n==1) return 1; // Used && instead of || at first
    int *a=calloc(n+1,sizeof(int)); // Used n instead of n-1 first
    a[0]=1; // Put int in front at first
    a[1]=1;
    int c=2;
    while(c<=n) {
        for(int i=0;i<c;i++) a[c]+=a[i]*a[c-1-i];
        c++; // Forgot to increment c at first
    }
    return a[n]; // Used c at first
}