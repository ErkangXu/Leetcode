int majorityElement(int num[], int n) {
    int number=0;
    int count=0;
    for(int i=0;i<n;i++) {
        if(count==0 || num[i]==number){
            number=num[i];
            count++;
        } else {
            count--;
        }
    }
    return number;
}