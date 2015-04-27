void nextPermutation(int num[], int n) {
    if(n==1 || n==0) return;
    int i=n-2;
    while(i>=0){
        for(int j=i+1;j<n;j++){
            if(num[j]>num[i]){
                int tmp=num[j];
                num[j]=num[i];
                num[i]=tmp;
                return;
            }
        }
        int tmp=num[i];
        for(int k=i;k<n-1;k++) num[k]=num[k+1];
        num[n-1]=tmp;
        i--;
    }
}