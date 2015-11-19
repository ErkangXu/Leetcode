public class Solution {
    public int maxProfit(int k, int[] prices) {
        if(k==0) return 0;
        List<Integer> lowList = new ArrayList<Integer>();
        List<Integer> highList = new ArrayList<Integer>();
        int i=0;
        int maxProfit=0;
        while (i<prices.length-1){
            while(i<prices.length-1 && prices[i]>=prices[i+1]) i++;
            if (i==prices.length-1) break;
            int low=prices[i];
            lowList.add(low);
            while(i<prices.length-1 && prices[i]<=prices[i+1]) i++;
            maxProfit+=prices[i]-low;
            highList.add(prices[i]);
        }
        while (lowList.size()>k) {
            int minOverlap=Integer.MAX_VALUE;
            int overlapPosition=-1;
            int minSingleProfit=Integer.MAX_VALUE;
            int minSPPosition=-1;
            for(int j=0;j<lowList.size()-1;j++){
                if(highList.get(j)-lowList.get(j+1)<minOverlap){
                    minOverlap=highList.get(j)-lowList.get(j+1);
                    overlapPosition=j;
                }
                if(highList.get(j)-lowList.get(j)<minSingleProfit){
                    minSingleProfit=highList.get(j)-lowList.get(j);
                    minSPPosition=j;
                }
            }
            int lastProfit=highList.get(highList.size()-1)-lowList.get(lowList.size()-1);
            if(lastProfit<minSingleProfit){
                minSingleProfit=lastProfit;
                minSPPosition=highList.size()-1;
            }
            if(minOverlap<minSingleProfit) {
                maxProfit-=minOverlap;
                highList.set(overlapPosition,highList.get(overlapPosition+1));
                highList.remove(overlapPosition+1);
                lowList.remove(overlapPosition+1);
            } else {
                maxProfit-=minSingleProfit;
                highList.remove(minSPPosition);
                lowList.remove(minSPPosition);
            }
        }
        return maxProfit;
    }
}