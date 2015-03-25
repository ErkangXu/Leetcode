char *addBinary(char *a, char *b) {
    if (!*a) return b;
    if (!*b) return a;
    int la=0;
    char * ta=a;
    while(*ta) {
         ta++;
         la++;
    }
    int lb=0;
    char * tb=b;
    while(*tb){
        tb++;
        lb++;
    }
    int lc=(la>lb)?la:lb;
    char * r=malloc((lc+2)*sizeof(char));
    int cr = 0;
    for(int i=0;i<lc+1;i++) {
        char ca = (i<la)?*(--ta):'0';
        char cb = (i<lb)?*(--tb):'0';
        if(ca=='1' && cb=='1') {
            if (cr==1) {
                *r++='1';
            } else {
                *r++='0';
            }
            cr=1;
        } else if (ca=='1' || cb=='1') {
            if (cr==1) {
                *r++='0';
                cr=1;
            } else {
                *r++='1';
                cr=0;
            }
        } else {
            if (cr==1) {
                *r++='1';
            } else {
                *r++='0';
            }
            cr=0;
        }
    }
    char * rr=malloc((lc+2)*sizeof(char));
    char * rrr=rr;
    if (*(--r)=='1') *(rr++)='1';
    for (int j=0;j<lc;j++) {
        *(rr++)=*(--r);
    }
    *rr='\0';
    return rrr;
}