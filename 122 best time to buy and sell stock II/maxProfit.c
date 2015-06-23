int maxProfit(int* prices, int pricesSize) {
    if(pricesSize<2) return 0;
    int index=1;
    int valley=prices[0];
    int profit=0;
    while(index<pricesSize){
        while(index<pricesSize && prices[index]<prices[index-1]) valley=prices[index++];
        while(index<pricesSize && prices[index]>=prices[index-1]) index++;
        profit+=prices[index-1]-valley;
    }
    return profit;
}