public class Solution {
    List<List<Integer>> result;
    int len;

    void pick(int st, int n, List<Integer> list){
        if(n==0) {
            result.add(list);
            return;
        }
        for(int i=st;i<len-n+2;i++){
            List<Integer> nL = new ArrayList<Integer>(list);
            nL.add(i);
            pick(i+1,n-1,nL);
        }
    }

    public List<List<Integer>> combine(int n, int k) {
        if(n==0 || k>n) return null;
        len=n;
        result= new ArrayList<List<Integer>>();
        List<Integer> ip = new ArrayList<Integer>();
        pick(1,k,ip);
        return result;
    }
}
