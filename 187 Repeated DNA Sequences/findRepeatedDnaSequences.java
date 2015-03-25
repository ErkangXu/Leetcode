public class Solution {
    /*
    public List<String> findRepeatedDnaSequences(String s) {
        ArrayList<String> re = new ArrayList<String>();
        int len = s.length();
        if(len<10) return re;
        HashSet<String> set = new HashSet<String>();  // It takes to much space to store all the String
        HashSet<String> rs = new HashSet<String>();
        for(int i=0;i<=9 && i<len-9;i++){
            for(int j=i;j<len-9;j=j+10){
                String s2 = s.substring(j,j+10);
                if(!set.contains(s2)) {
                    set.add(s2);  // And it takes too much time to hash the string every time
                } else {
                    rs.add(s2);
                }
            }
        }
        re = new ArrayList<String>(rs);
        return re;
    }
    */
    private static HashMap<Character,Integer> charHashcodeTable = new HashMap<Character,Integer>();
    static{charHashcodeTable.put('A',0); charHashcodeTable.put('C',1); charHashcodeTable.put('G',2); charHashcodeTable.put('T',3);}
    private static final int SIZE_POW_9 = (int) Math.pow(charHashcodeTable.size(),9); // Need to do the conversion, in Java int is 32bit
    public List<String> findRepeatedDnaSequences(String s) {
        HashSet<Integer> rhashs = new HashSet<Integer>();
        HashSet<String> rs = new HashSet<String>();
        for(int i=0 , rhash=0; i<s.length(); i++){ // Only use , to separate two same type variables, and you can't specify the type again
            if(i>9) rhash-= SIZE_POW_9*charHashcodeTable.get(s.charAt(i-10));
            rhash=rhash*charHashcodeTable.size()+charHashcodeTable.get(s.charAt(i));
            if(i>8 && !rhashs.add(rhash))  rs.add(s.substring(i-9,i+1));
        }
        return new ArrayList<String>(rs);
    }
}