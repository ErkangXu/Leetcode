int minPathSum(int** grid, int gridRowSize, int gridColSize) {
    for(int i=1;i<gridColSize;i++) grid[0][i]+=grid[0][i-1];
    for(int j=1;j<gridRowSize;j++) grid[j][0]+=grid[j-1][0];
    for(int j=1;j<gridRowSize;j++) {
        for(int i=1;i<gridColSize;i++) grid[j][i]+= (grid[j][i-1]<grid[j-1][i])? grid[j][i-1]:grid[j-1][i];
    }
    return grid[gridRowSize-1][gridColSize-1];
}