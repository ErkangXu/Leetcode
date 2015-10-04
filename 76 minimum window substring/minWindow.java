public class Solution {
    public String minWindow(String s, String t) {
        Map<Character,Integer> map = new HashMap<Character,Integer>();
        for(int i=0;i<t.length();i++){
            char c=t.charAt(i);
            if(map.containsKey(c))
                map.put(c,map.get(c)+1);
            else
                map.put(c,1);
        }
        Map<Character,Integer> map1 = new HashMap<Character,Integer>(map);
        Map<Character,Integer> map2 = new HashMap<Character,Integer>();
        int i=0;
        int len=s.length();
        LinkedList<Integer> queue = new LinkedList<Integer>();
        while(i<len && !map1.isEmpty()){
            char z=s.charAt(i);
            if(map.containsKey(z)) {
                if(map1.containsKey(z)) {
                    if(map1.get(z)==1)
                        map1.remove(z);
                    else
                        map1.put(z,map1.get(z)-1);
                } 
                queue.add(i);
                if(map2.containsKey(z))
                    map2.put(z,map2.get(z)+1); // It's map2 here, not map
                else
                    map2.put(z,1);
            }
            i++;
        }
        if(!map1.isEmpty()) return "";
        int bestStart=queue.peek();
        int bestEnd=i-1; // Can't use i, because it's a queue of exact index
        
        while(true){
            int j=queue.peekLast()+1; // Put the line here in case t has only one char
            char firstChar=s.charAt(queue.pop()); 
            if(map2.get(firstChar)>1)
                map2.put(firstChar,map2.get(firstChar)-1); // Need to consider the situation where
            else
                map2.remove(firstChar);
            if(map2.containsKey(firstChar) && map2.get(firstChar)-map.get(firstChar)>=0) {
                if(queue.peekLast()-queue.peek()<bestEnd-bestStart){
                    bestStart=queue.peek();
                    bestEnd=queue.peekLast();
                }
                continue;
            }
            while(j<len) {
                char rc=s.charAt(j);
                if(map.containsKey(s.charAt(j))){
                    queue.add(j);
                    if(map2.containsKey(rc)) // not firstChar here
                        map2.put(rc,map2.get(rc)+1);
                    else
                        map2.put(rc,1);  // map2 not map
                    if(s.charAt(j)==firstChar) {
                        if(j-queue.peek()<bestEnd-bestStart){
                            bestStart=queue.peek();
                            bestEnd=j;
                        }
                        break;
                    }
                }
                j++;
            }
            if(j>=len) break;
        }
        return s.substring(bestStart,bestEnd+1);
    }
}