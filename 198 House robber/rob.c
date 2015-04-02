int rob(int num[], int n) {
    if(n==0) return 0;
    if(n==1) return num[0]; // Handles corner cases
    int mon[n];
    mon[0]=num[0];
    mon[1]=num[1];
    mon[2]=num[2]+mon[0];
    for(int i=3;i<n;i++){
        mon[i]=(mon[i-2]>mon[i-3])? mon[i-2]:mon[i-3];
        mon[i]+=num[i]; // The robber can have two house as interval
    }
    return mon[n-1]>mon[n-2]? mon[n-1] : mon[n-2]; // need to compare the last two points
}