void rotate(int **matrix, int n) {
    int layer = (n+1)/2;
    for(int i=0;i<=layer;i++){
        int range=n-1-i*2;
        int bnd=n-1-i;
        for(int j=0;j<range;j++){
            int tmp=matrix[i][i+j]; // Put the tmp variable inside actually makes the code faster
            matrix[i][i+j]=matrix[bnd-j][i];
            matrix[bnd-j][i]=matrix[bnd][bnd-j];
            matrix[bnd][bnd-j]=matrix[i+j][bnd];
            matrix[i+j][bnd]=tmp;
        }
    }
}