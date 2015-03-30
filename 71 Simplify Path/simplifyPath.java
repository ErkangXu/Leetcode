public class Solution {
    public String simplifyPath(String path) {
        LinkedList<String> stack = new LinkedList<String>();
        String[] stringArray = path.split("/");
        for(int i=0; i<stringArray.length; i++) { // forgot to initialize i
            String tmp = stringArray[i];
            if(tmp.equals(".") || tmp.equals("")) {
                continue;
            }else if(tmp.equals("..")) {
                stack.pollLast();
            } else {
                stack.add(tmp);
            }
        }
        StringBuilder sb = new StringBuilder();
        for(String s:stack){
            sb.append("/");
            sb.append(s);
        }
        if(sb.length()==0) sb.append("/");
        return sb.toString();
    }
}