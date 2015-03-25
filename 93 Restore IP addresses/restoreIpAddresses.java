public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> resultList = new ArrayList<String>();
        int len = s.length();
        if(len<4) return resultList;
        StringBuffer sb = new StringBuffer();
        for(int i=1;i<4;i++){ // the substring method, the right bound is exclusive
            String st1 = s.substring(0,i);  // the method is substring, no camel case
            int v1 = Integer.parseInt(st1);
            if(v1>255 || (st1.charAt(0)=='0' && st1.length()>1)) {
                break;
            }

            for(int j=i+1;j<i+4;j++){
                if(j>len-2) break;
                String st2 = s.substring(i,j);
                int v2 = Integer.parseInt(st2);
                if(v2>255 || (st2.charAt(0)=='0' && st2.length()>1)) {
                    break;
                }
                
                for(int k=j+1;k<j+4;k++){
                    if(k<len-4) continue;
                    if(k>len-1) break;
                    String st3 = s.substring(j,k);
                    int v3 = Integer.parseInt(st3);
                    if(v3>255 || (st3.charAt(0)=='0' && st3.length()>1)) {
                        break;
                    }
                    String st4 = s.substring(k,len);
                    int v4 = Integer.parseInt(st4);     // Here mispelled to st3 at first
                    if(v4>255 || (st4.charAt(0)=='0' && st4.length()>1)) {
                        continue; // I used break here at first. If the last octave is too long, we should continue to shorten it
                    }
                    String indr=st1+"."+st2+"."+st3+"."+st4;
                    resultList.add(indr);
                }
            }
        }
        return resultList;
    }
}