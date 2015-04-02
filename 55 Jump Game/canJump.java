public class Solution {
    public boolean canJump(int[] A) {
        int max=0;
        for(int i=0; i<=max; i++){
            if(A[i]+i>=A.length-1) return true;
            if(A[i]+i>max) max=A[i]+i; // Miswrote it as 1 instead of i
        }
        return false;
    }
}