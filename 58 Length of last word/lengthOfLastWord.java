public class Solution {
    public int lengthOfLastWord(String s) {
        int p=s.length()-1;
        while(p>-1 && s.charAt(p)==' ') p--; // Deals with trailing spaces
        int q=p;
        while(p>-1 && s.charAt(p)!=' ') p--;
        return q-p;
    }
}