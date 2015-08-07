void setZeroes(int** matrix, int matrixRowSize, int matrixColSize) {
    int mark;
    int flag=1;
    while (flag==1){
        mark = rand();
        flag=0;
        for(int i=0; i<matrixRowSize; i++) for(int j=0; j<matrixColSize; j++) if(matrix[i][j]==mark) {
            flag=1;
            break;
        }
    }
    for(int i=0; i<matrixRowSize; i++) {
        for(int j=0; j<matrixColSize; j++) {
            if(matrix[i][j]==0){
                for(int m=0; m<matrixRowSize; m++) if(matrix[m][j]!=0) matrix[m][j]=mark;
                for(int m=0; m<matrixColSize; m++) if(matrix[i][m]!=0) matrix[i][m]=mark;
            }
        }
    }
    for(int i=0; i<matrixRowSize; i++) for(int j=0; j<matrixColSize; j++) if(matrix[i][j]==mark) matrix[i][j]=0;
}