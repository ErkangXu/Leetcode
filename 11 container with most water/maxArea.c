int maxArea(int* height, int heightSize) {
    int lm=0;
    int ld=0; // The left bound when got the max value last time
    int rm=heightSize-1;
    int rd=rm;
    int maxC=0;
    while(lm<rm){
        int shortE=(height[lm]<height[rm])? height[lm]:height[rm];
        int area=shortE*(rm-lm);
        if(area>maxC) {
            maxC=area;
            ld=lm;
            rd=rm;
        }
        if(height[lm]<height[rm]){
            while(height[lm+1]<=height[ld]) lm++;
            lm++; // Move it to a edge that is longer than the previous one
        }else {
            while(height[rm-1]<=height[rd]) rm--;
            rm--;
        }
    }
    return maxC;
}
