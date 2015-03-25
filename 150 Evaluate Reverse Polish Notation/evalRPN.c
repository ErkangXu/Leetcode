int evalRPN(char *tokens[], int n) {
    int stack[5000];
    int position=-1;
    int tmp;
    for(int i=0; i<n; i++){
        if((tokens[i][0] == '-' && strlen(tokens[i])!=1) || (tokens[i][0]>= '0' && tokens[i][0]<='9')) {
            sscanf(tokens[i],"%d",&tmp);
            stack[++position]=tmp;
            continue;
        }
        int op2 = stack[position];
        int op1 = stack[--position];
        if(tokens[i][0] == '+') {
            stack[position]=op1+op2;
        } else if (tokens[i][0] == '-') {
            stack[position]=op1-op2;
        } else if(tokens[i][0] == '*') {
            stack[position]=op1*op2;
        } else if(tokens[i][0] == '/') {
            stack[position]=op1/op2;
        }
    }
    return stack[0];
}