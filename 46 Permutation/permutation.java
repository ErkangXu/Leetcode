public class Solution {
    List<List<Integer>> result;
    int len;
    public void pick(List<Integer> inp, List<Integer> cand) {
        if(inp.size()==len) {
            result.add(inp);
            return;
        }
        for(int i=0;i<cand.size();i++){
            List<Integer> nCand= new ArrayList<Integer>(cand);
            List<Integer> nInp=new ArrayList<Integer>(inp);
            nInp.add(nCand.remove(i));
            pick(nInp,nCand);
        }
    }
    public List<List<Integer>> permute(int[] nums) {
        if(nums.length==0) return null;
        result=new ArrayList<List<Integer>>();
        len=nums.length;
        List<Integer> candidates = new ArrayList<Integer>();
        for(int i=0;i<len;i++) candidates.add(nums[i]);
        List<Integer> initialList = new ArrayList<Integer>();
        pick(initialList, candidates);
        return result;
    }
}