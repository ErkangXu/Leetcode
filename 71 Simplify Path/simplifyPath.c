char *simplifyPath(char *path) {
    char *re=malloc(strlen(path)*sizeof(char));
    char *sp=re;
    int pStack[100]; // Some of the paths are very deep, need to use 100 here 
    int p=0;
    pStack[0]=0; // / handle the situation like "/home/../../.."
    while(*(path)!='\0' && *(path+1)!='\0') { // adding *(path+1)!='\0' reduces the runtime, it handles the trailing /
        while (*path!='\0' && (*(path+1)=='.' || *(path+1)=='/')) {
            if (*(path+1)=='/') {
                path++;
            } else if(*(path+1)=='.' && *(path+2)=='.' && (*(path+3)=='/' || *(path+3)=='\0')) {
                re=sp+pStack[p]; // reset the output pointer
                p=(p==0)? 0:p-1; // handle the situation like "/home/../../.."
                path+=3;
            } else if(*(path+1)=='.' && (*(path+2)=='/' || *(path+2)=='\0')) { // miswrote +2 as +1
                path+=2;
            } else break; // Some of the input has illegal input like "..." in the end, need to ignore that
        }
        if (*path=='\0' || *(path+1)=='\0') break; // Heandles the situation where the last character is '/'
        pStack[++p]=re-sp;
        do {
            *re++=*path++;
        } while(*path!='/' && *path!='\0'); //forgot ; didn't consider the situation where path terminated in the first loop
    }
    if(re==sp) *re++='/'; // handle the situation like "/home/../../.."
    *re='\0';
    return sp;
}