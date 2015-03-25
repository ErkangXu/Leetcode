#include <stdio.h>

void merge(int* pi, int low, int high) {
    int l = high - low +1;
    int tmp[l];
    for(int i=low;i<=high;i++){
        tmp[i-low]=pi[i];
    }
    int i,m,j,k;
    i=low;
    m=(low+high)/2+1;
    j=m;
    k=low;
    while(i<m && j<=high) {
        if(tmp[i-low]<=tmp[j-low]){
            pi[k]=tmp[i-low];
            i++;
        } else {
            pi[k]=tmp[j-low];
            j++;
        }
        k++;
    }
    for(int d=i; d<m; d++) {
        pi[k++]=tmp[d-low];
    }
}

void mergesort(int* pi, int low, int high) {
    if (low<high) {
        mergesort(pi, low, (low+high)/2);
        mergesort(pi, (low+high)/2+1, high);
        merge(pi,low,high);
    }
}

int *twoSum(int numbers[], int n, int target) {
    int h[n];
    for(int i=0;i<n;i++){
        h[i]=numbers[i];
    }
    mergesort(h, 0, n-1);

    int l=n-1;
    int j,k;
    for(j=0;j<n;j++){
        for(k=l; k>0; k--) {
            if(*(h+j)+*(h+k)==target) {
                goto out;
            }else if(*(h+j)+*(h+k)<target) {
                l=k;
                break;
            }
        }
    }
    out:;

    int n1=*(h+j);
    int n2=*(h+k);

    int i1,i2;
    int z;
    for(z=0;z<n;z++){
        if(*(numbers+z)==n1){
            i1=z+1;
            break;
        }
    }
    for (z=0;z<n;z++){
        if (*(numbers+z)==n2 && z!=i1-1){
            i2=z+1;
            break;
        }
    }
    int r[2];
    if(i1<i2) {
        *(r)=i1;
        *(r+1)=i2;
    } else {
        *(r)=i2;
        *(r+1)=i1;
    }
    return r;
}