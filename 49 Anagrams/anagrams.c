struct countEntry {
    char* sortedString;
    int indices[20];
    UT_hash_handle hh; // It's handle not handler
};

void sortHelper(char* in, int s, int e){
    if(s>=e) return;
    int m = (s+e)/2;
    char mc = in[m];
    int f=s,b=e; // I used f=0 at first
    while(f<=b){ // f and b stop at the same position which value equals mc, need to use = here
        while(in[f]<mc) f++;
        while(in[b]>mc) b--; // can't use = in quick sort, it might cause ifinite loops
        if(f>b) break;
        char te = in[f];
        in[f++]=in[b];
        in[b--]=te;
    }
    sortHelper(in,s,f-1);
    sortHelper(in,f,e);
}

char* sort(char* f, bool s) { // if s is false, just copy the string
    char* it = f;
    int len = strlen(f);
    char* re=calloc((len+1),sizeof(char)); // calloc has two arguments
    strcpy(re,f);
    if(s==true) sortHelper(re, 0,len-1); // should not sort the \0 character, sort the string when if the switch is true
    return re;
}

char **anagrams(char *strs[], int n, int *outputSize) {
    char** result=malloc(n*sizeof(char*));
    struct countEntry *s, *countTable = NULL; // * should go with the variable name
    int p=0;
    for(int i=0;i<n;i++){
        char* tm = sort(strs[i],true);
        HASH_FIND_STR(countTable, tm, s);
        if(s==NULL){
            s = (struct countEntry*)malloc(sizeof(struct countEntry));
            s->sortedString = tm;
            s->indices[0] = i;
            s->indices[1] = -1; // use -1 to indicate the end of the list
            HASH_ADD_KEYPTR(hh, countTable, s->sortedString, strlen(s->sortedString), s);
        } else {
            int j=0;
            while(s->indices[j]!=-1) j++;
            s->indices[j]=i;
            s->indices[j+1]=-1;
        }
    }
    for(s=countTable; s != NULL; s=s->hh.next) {
        if(s->indices[1]!=-1) {
            for(int k=0; s->indices[k]!=-1;k++) { // Forgot yo initialize k to 0 at first
                result[p++]=sort(strs[s->indices[k]],false);
            }
        }
    }
    *outputSize=p;
    return result;
}