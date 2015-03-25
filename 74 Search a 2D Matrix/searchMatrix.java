public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix[0][0]>target) return false;
        int numr = matrix.length;  // Getting length of array uses length with out the brackets
        int rnum = searchRow(matrix,0,numr-1,target);
        int numc = matrix[0].length;
        return searchColumn(matrix,rnum,0,numc-1,target);
    }
    public int searchRow(int[][] matrix,int start,int finish, int target) {
        /*if(start==finish) {
            if (matrix[start][0]>target) { // Used 0 instead of target at first
                return start-1;
            } else {
                return start;
            }
        } */   //The commented situation would be handled by the following statement
        if(start>finish) return start-1;      // for the situation of target out of bound, use finish is the same
        int mi=(start+finish)/2;
        if (matrix[mi][0]>target) {
            return searchRow(matrix, start,mi-1,target); 
        } else if (matrix[mi][0]<target) {
            return searchRow(matrix, mi+1,finish,target);
        } else {
            return mi;   // Arranging the conditions like this can speed up the code, we shoud put the most likely situation front
        }
    }
    public boolean searchColumn(int[][] matrix, int rown, int start,int finish, int target) {
        if(start>finish) return false; // This is for out of bound error
        int mi=(start+finish)/2;
        if (matrix[rown][mi]>target) {
            return searchColumn(matrix, rown, start,mi-1,target); 
        } else if (matrix[rown][mi]<target) {
            return searchColumn(matrix, rown, mi+1,finish,target);
        } else {
            return true;
        }
    }
}