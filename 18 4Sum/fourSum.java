public class Solution {
    public class Pair {
        int first;
        int second;
        public Pair(int f,int s) {
            first=f;
            second=s;
        }
        public boolean isOverlap(Pair another) {
            if (first==another.first || second==another.first || first==another.second || second==another.second) return true;
            return false;
        } 
    }
    public List<List<Integer>> fourSum(int[] num, int target) {
        int len = num.length;
        if (len<4) return new ArrayList<List<Integer>>();
        Set<List<Integer>> rs = new HashSet<List<Integer>>();
        Map<Integer,ArrayList<Pair>> map = new TreeMap<Integer,ArrayList<Pair>>();
        for(int i=0;i<len;i++){
            for(int j=i+1;j<len;j++) {
                int sum = num[i]+num[j];
                if(map.containsKey(sum)){
                    map.get(sum).add(new Pair(i,j));
                } else {
                    ArrayList<Pair> tp = new ArrayList<Pair>();
                    tp.add(new Pair(i,j));
                    map.put(sum,tp);
                }
            }
        }
        for(Integer key:map.keySet()){
            int dif=target-key;
            if(dif>=key && map.containsKey(dif)) { // containsKey not contains
                Iterator<Pair> ip = map.get(key).iterator();
                while(ip.hasNext()){
                    Pair x=ip.next();
                    ip.remove(); // remove method doesn't need parameters
                    for(Pair p : map.get(dif)){
                        if(x.isOverlap(p)) continue;
                        List mem = new ArrayList<Integer>();
                        mem.add(num[x.first]);
                        mem.add(num[x.second]);
                        mem.add(num[p.first]);
                        mem.add(num[p.second]);
                        Collections.sort(mem);
                        rs.add(mem);
                    }
                }
            }
        }
        List<List<Integer>> rl = new ArrayList<List<Integer>>(rs);
        return rl;
    }
}