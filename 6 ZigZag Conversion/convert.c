char *convert(char *s, int nRows) {
    if (s==NULL) return s; // I missed one = here at first. You can return s(the input parameter) only if it's NULL
    int slen = strlen(s); // You can use strlen on a empty string as well 
    char *sp = malloc((slen+1)*sizeof(char)); // Allocate space for the return string
    if(*s=='\0') { // You can use slen==0 here as well
        *sp = '\0';
        return sp; // For the return pointer, you have to point to a place you allocated.
    }
    if (nRows==1) {
        char* t = sp;
        while(*s!='\0'){
            *t++=*s++;
        }
        *t='\0';
        return sp;
    }
    char* array[nRows]; // Array of pointers to different lines
    int pa[nRows]; // Index to those pointers, because you can't move those pointers around
    for(int i=0;i<nRows;i++){
        array[i]=malloc(100*sizeof(char)); // 100 might not be enough, but using (slen+1) exceeds the memory limit
        pa[i]=0;
    }
    int di = 0; // indicate direction
    int rn=0; // row number
    while (*s!='\0') {
        *(array[rn]+pa[rn])=*s++;
        pa[rn]=pa[rn]+1;
        if(di==0){
            rn++;
            if (rn==nRows-1) di=1; // If reach the last line, change direction
        } else {
            rn--;
            if (rn==0) di=0;
        }
    }
    for(int i=0;i<nRows;i++){
        *(array[i]+pa[i])='\0';
    }
    char * rt =sp; // We keep the position of sp, and just move rt around
    char* tmp;
    for(int i=0;i<nRows;i++){
        tmp = array[i];
        while(*tmp!='\0') {    // I put =! here before
            *(rt++)=*(tmp++);
        }
    }
    *rt='\0';
    return sp;
}