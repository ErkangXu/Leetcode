public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
        if (s=="" || dict.isEmpty()) return false;
        int len = s.length();
        /*
        Set<Character> charSet1 = new HashSet<Character>();
        for(int i=0; i<len; i++){
            char tmp = s.charAt(i);
            if(!charSet1.contains(tmp)) charSet1.add(tmp);
        }
        Set<Character> charSet2 = new HashSet<Character>();
        */
        int maxL=0;
        for(String word: dict){
            int chang = word.length();
            if(chang>maxL) maxL=chang;
            /*
            for(int i=0; i<chang; i++){
                char tmp = word.charAt(i);
                if(!charSet2.contains(tmp)) charSet2.add(tmp);
            }
            */
        }
        //if(!charSet2.containsAll(charSet1)) return false;      // Actually no need for this char set chect, it made code slower
        Set<Integer> lastG = new HashSet<Integer>(); // Available starting point check
        lastG.add(0); // Need to set the first starting point
        for(int i=1;i<=len;i++){
            lastG.remove(i-maxL-1);
            if(lastG.isEmpty()) return false;
            boolean fl = false;
            for(Integer l:lastG) {
                if(dict.contains(s.substring(l,i))) {
                    fl=true;
                    break;
                }
            }
            if(fl==true) lastG.add(i);
        }
        return lastG.contains(len); // Starting point is the the last cutting point as well, len has to be a cutting point
    }
}