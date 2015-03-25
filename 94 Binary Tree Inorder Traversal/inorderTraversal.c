 // Definition for binary tree
 // struct TreeNode {
  //    int val;
  //    struct TreeNode *left;
  //    struct TreeNode *right;
  //};

int *inorderTraversal(struct TreeNode *root, int *returnSize) {
    if (root==NULL){
        *returnSize=0;
        return NULL;
    }
    //int *r; This is not gonna work, int r[1000]; won't either
    int *r=malloc(1000*sizeof(int));
    struct TreeNode * stack[1000];

    int i=0;
    int p=-1;
    struct TreeNode * cur = root;
    while (cur!=NULL || p>=0) {
        while(cur!=NULL) {
            stack[++p]=cur;
            cur=cur->left;
        }
        cur=stack[p--];
        r[i++]=cur->val;
        cur=cur->right;
    }
    *returnSize=i;
    return r;
}