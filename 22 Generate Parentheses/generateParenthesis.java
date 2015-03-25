public class Solution {
    public List<String> generateParenthesis(int n) {
        List<ArrayList<String>> r = new ArrayList<ArrayList<String>>(n+1);
        ArrayList<String> r0 = new ArrayList<String>();
        r0.add("");
        if(n==0) return r0;
        ArrayList<String> r1 = new ArrayList<String>();
        r1.add("()");
        if(n==1) return r1;
        ArrayList<String> r2 = new ArrayList<String>();
        r.add(r0);
        r.add(r1);
        r.add(r2);
        int i=2;
        while(true){
            List<String> si = r.get(i);
            for(int j=0;j<i;j++){
                for(String s: r.get(j)) {
                    for (String ss: r.get(i-j-1)) {
                        StringBuffer sb = new StringBuffer();
                        sb.append("(");
                        sb.append(s);
                        sb.append(")");
                        sb.append(ss);
                        si.add(sb.toString());
                    }
                }
            }
            if(n==i) return si;
            i++;
            ArrayList<String> tp = new ArrayList<String>();
            r.add(tp);
        }
    }
}