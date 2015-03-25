int lengthOfLongestSubstring(char *s) {
    if(!*s) return 0;
    int ck[256];
    for(int j=0; j<256 ; j++) {
         ck[j]=-1;
    }
    int cd=strlen(s);
    int maxv=0;
    int len=0;
    for(int i=0; i<cd ; i++,len++) {
        if(s[i]=='\0') break;
        int n = (int)s[i];
        if(ck[n]>=0){
            if(len>maxv) maxv=len;
            i = ck[n];
            for(int j=0; j<256 ; j++) {
                ck[j]=-1;
            }
            len=-1;
        } else {
            ck[n]=i;
        }
    }
    return (maxv>(len))? maxv:(len);
}