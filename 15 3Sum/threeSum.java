public class Solution { 
    boolean exist(int[] nums, int target, int start, int end) {
        if(target>nums[end] || target<nums[start]) return false;
        int mid=(start+end)/2; 
        if (nums[mid]==target) return true; 
        if (nums[mid]<target) return exist(nums,target,mid+1,end); 
        return exist(nums,target,start,mid-1); 
    } 
    public List<List<Integer>> threeSum(int[] nums) { 
        Arrays.sort(nums); 
        List<List<Integer>> result = new ArrayList<List<Integer>>(); 
        int e=nums.length-1; 
        while(1<e){ 
            int ev=nums[e];
            int f=0;
            while(f<e-1){
                int fv=nums[f];
                int ts=-fv-ev; 
                if(ts<nums[f+1]) {
                    break;
                } 
                if(exist(nums,ts,f+1,e-1)) { 
                    List<Integer> tmp = new ArrayList<Integer>(); 
                    tmp.add(fv); 
                    tmp.add(ts); 
                    tmp.add(ev); 
                    result.add(tmp); 
                } 
                while(f<=e-1 && nums[f]==fv) f++; // should guard f
            }
            while(e>1 && nums[e]==ev) e--; // should guard e as well
        }
        return result;
    } 
}
