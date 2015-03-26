int uniquePaths(int m, int n) {
    int* grid=malloc(m*n*sizeof(int)); //It's hard to allocate memory for a 2 dimensional array, so I flattened it
    for (int i=0; i<n; i++) grid[i]=1;
    for (int i=0; i<m; i++) grid[i*n]=1;
    for (int i=1;i<m;i++) {
        for(int j=1;j<n;j++) grid[i*n+j]=grid[(i-1)*n+j]+grid[i*n+j-1];
    }
    return grid[(m-1)*n+n-1]; 
}