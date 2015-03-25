int maxProduct(int A[], int n) {
    if(n==1) return A[0]; // I used = instead of == here before
    int m[n];
    m[0]=A[0];
    for(int i=1;i<n;i++){
        if(m[i-1]==0) {
            m[i]=A[i];
        } else {
            m[i]=m[i-1]*A[i];
        }
    }
    int max=-32768;
    int np=-1;
    int mm=0; // Why I was so stupid, the whole number is defnitely larger than it divided by a positive integer
    for(int i=0;i<n+1;i++){ // I added one more loop to reuse the code that updates the max
        if(i==n || m[i]==0) { // I used = instead of == here before
            if (i!=n && max<0) max=0; // I didn't put this line here at first. 0 is a valid result as well
            if(m[i-1]==0 || i==0) continue; // I used = instead of == here before
            if(m[i-1]>0){
                if(m[i-1]>max) max=m[i-1];
            } else {
                if(np==i-1) {
                    if(mm!=0) {
                        if(mm>max) max=mm;
                    } else {
                        if(m[i-1]>max) max=m[i-1];
                    }
                } else {
                    int tmp = m[i-1]/m[np];
                    if(mm!=0) {
                        if(mm>tmp) tmp=mm;
                    }
                    if(tmp>max) max=tmp;
                }
            }
            np=-1;
            mm=0;
        } else if(m[i]>0){
            mm=m[i];
        } else if (np==-1){
            np=i;
        }
    }
    return max; // The m array is segregatted by 0, in those segments, the magnitude is non-decreasing
}