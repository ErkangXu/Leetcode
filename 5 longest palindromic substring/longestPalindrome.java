public class Solution {
    public String longestPalindrome(String s) {
        int len=s.length();
        if(len==1) return s;
        int lastH=0;
        int x=0;
        for(int i=0;i<len-1;i++){
            int k=0;
            int j=0;
            while(i+k+2<len && i-k>=0 && s.charAt(i+k+2)==s.charAt(i-k)) k++;
            while(i+j+1<len && i-j>=0 && s.charAt(i+j+1)==s.charAt(i-j)) j++;
            if(2*k+1>lastH && 2*k+1>2*j) {
                lastH=2*k+1;
                x=i-k+1;
            } else if(2*j>lastH && 2*j>2*k+1){
                lastH=2*j;
                x=i-j+1;
            }
        }
        return s.substring(x,x+lastH);
    }
}
