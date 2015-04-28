class Solution {
    public String multiply(String num1, String num2) {
        int s1=num1.length(); // Solution using arrays instead of ArrayList and iterate on string directly
        int s2=num2.length();
        int[] result=new int[s1+s2]; // The maximum size of the result will be s1+s2
        for(int j=0;j<s2;j++) {
            int c=0;
            int out=Character.getNumericValue(num2.charAt(s2-1-j)); // should do it from the tail of the string
            for(int i=0;i<s1;i++){
                int in=Character.getNumericValue(num1.charAt(s1-1-i));
                int r=in*out+result[i+j]+c;
                int s=r%10;
                c=r/10;
                result[i+j]=s;
            }
            if(c>0) result[j+s1]=c;
        }
        StringBuilder sb=new StringBuilder();
        int i=result.length-1;
        while(i>0 && result[i]==0) i--; // Handle when there are leading 0s, and it could be all 0s
        while(i>=0) sb.append(result[i--]);
        return sb.toString();
    }
}
