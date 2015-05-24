public class Solution {
    public int numDecodings(String s) {
        int len=s.length();
        if(len==0 || s.charAt(0)=='0') return 0;
        if(len==1) return 1;
        int firstC=1;
        int secondC=1;
        if(s.charAt(1)=='0') {
            if(s.charAt(0)>'2') return 0;
            firstC=0;
        } else {
            int twoDV=Character.getNumericValue(s.charAt(0))*10+Character.getNumericValue(s.charAt(1)); //Can't use (int) to cast char to its value
            if(twoDV<27) secondC=2;
        }
        if(len==2) return secondC;
        int[] counter = new int[len];
        counter[0]=firstC;
        counter[1]=secondC;
        for(int i=2;i<len;i++) {
            if(s.charAt(i)=='0') {
                if(s.charAt(i-1)=='0' || s.charAt(i-1)>'2') return 0;
                counter[i]=counter[i-2];
                counter[i-1]=0; //setting zero is very important;
            } else {
                counter[i]=counter[i-1];
                int twoDV=Character.getNumericValue(s.charAt(i-1))*10+Character.getNumericValue(s.charAt(i));
                if(twoDV<27) counter[i]+=counter[i-2];
            }
        }
        return counter[len-1];
    }
}