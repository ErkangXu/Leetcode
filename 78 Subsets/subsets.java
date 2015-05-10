c class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> nullList = new ArrayList<Integer>();
        result.add(nullList);
        int len = nums.length;
        if(len==0) return result;
        List<List<Integer>> levelList = new ArrayList<List<Integer>>();
        List<Integer> finalList = new ArrayList<Integer>(); // There is no ArrayList constructor using array
        for(int x:nums) finalList.add(x);
        Collections.sort(finalList);
        int lN=finalList.get(len-1);
        for(int i: finalList) {
            List<Integer> tmp = new ArrayList<Integer>();
            tmp.add(i);
            levelList.add(tmp);
        }
        result.addAll(levelList);
        for(int i=2;i<len;i++){ // Don't use = here, add the finalList in the end
            List<List<Integer>> newList = new ArrayList<List<Integer>>();
            for(List<Integer> l:levelList){
                int lastN=l.get(i-2); //Get the last/largest number in the list
                if(lastN<lN){
                    int index=finalList.indexOf(lastN);
                    for(int j=index+1;j<len;j++){
                        List<Integer> tmp = new ArrayList<Integer>(l);
                        tmp.add(finalList.get(j));
                        newList.add(tmp);
                    }
                }
            }
            result.addAll(newList);
            levelList=newList;
        }
        if(nums.length>1)result.add(finalList);
        return result;
    }
}
