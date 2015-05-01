public class Solution {
    public int factorial(int n){
        int p=1;
        while(n>0) p*=n--;
        return p;
    }
    public String getPermutation(int n, int k) {
        StringBuilder result = new StringBuilder();
        List<Integer> choices = new ArrayList<Integer>();
        for(int i=1;i<=n;i++) choices.add(i);
        for(int i=1;i<=n;i++){
            int f = factorial(n-i);
            if(f<k) {
                int d=(k-1)/f;
                result.append(choices.remove(d));
                k-=d*f;
            } else result.append(choices.remove(0));
        }
        return result.toString();
    }
}
