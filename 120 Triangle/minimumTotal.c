int minimumTotal(int **triangle, int numRows) {
    if(numRows==1) return **triangle;
    //int* row0=malloc(numRows*sizeof(int));
    //int* row1=malloc(numRows*sizeof(int));
    int row0[numRows];  // We can use both ways: declare array or allocate memory to pointer
    int row1[numRows];
    row0[0]=**triangle;
    int i;
    int min;
    for(i=1;i<numRows;i++){
        if(i%2==1) {
            row1[0]=row0[0]+triangle[i][0];

            for(int j=1;j<i;j++){
                if (row0[j-1]<row0[j]) {
                    row1[j]=row0[j-1]+triangle[i][j];
                } else {
                    row1[j]=row0[j]+triangle[i][j];
                }
            }
            row1[i]=row0[i-1]+triangle[i][i];
            
        } else {
            row0[0]=row1[0]+triangle[i][0];
            for(int j=1;j<i;j++){
                if (row1[j-1]<row1[j]) {
                    row0[j]=row1[j-1]+triangle[i][j];
                } else {
                    row0[j]=row1[j]+triangle[i][j];
                }
            }
            row0[i]=row1[i-1]+triangle[i][i];
        }
    }
    i--; // Need to take back the increment
    if (i%2==1) {
        min=row1[i--];
        while(i>=0){
            if (min>row1[i]) min=row1[i]; // Used == instead of = at first
            i--;
        }
    } else {
        min=row0[i--];
        while(i>=0){
            if (min>row0[i]) min=row0[i];
            i--;
        }
    }
    return min;
}