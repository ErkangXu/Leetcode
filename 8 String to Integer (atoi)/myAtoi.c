int myAtoi(char *str) {
    long val=0;
    int sign=1;
    while(*str==' ') str++; // Handles the leading spaces
    if(*str=='+') {
        sign=1;
        str++;
    } else if(*str=='-') { // Handles leading sign
        sign=-1;
        str++;
    }
    while(*str!=NULL){
        if(*str<'0' || *str>'9') break; // trailing non digits should not affect already converted part
        val=val*10+*(str++)-'0';
        if (sign*val>2147483647) { // handles overflow
            return 2147483647;
        } else if (sign*val<-2147483648){
            return -2147483648;
        }
    }
    return sign*val;
}