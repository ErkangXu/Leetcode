public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rowN=obstacleGrid.length;
        int columnN=obstacleGrid[0].length;
        int[][] pathGrid = new int[rowN][columnN];
        for(int i=0; i<rowN && obstacleGrid[i][0]==0; i++) pathGrid[i][0]=1;
        for(int i=0; i<columnN && obstacleGrid[0][i]==0; i++) pathGrid[0][i]=1;
        for(int i=1;i<rowN;i++){
            for(int j=1;j<columnN;j++){
                if(obstacleGrid[i][j]==0){
                    int pN=pathGrid[i][j-1]+pathGrid[i-1][j];
                    //if(pN==0) break; Can't save on break, if can't reach a point, doesn't mean can't reach points in its right
                    pathGrid[i][j]=pN;
                }
            }
        }
        return pathGrid[rowN-1][columnN-1];
    }
}
