/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* buildTreeHelper(int* preorder, int ps, int pe, int* inorder, int is, int ie) {
    if(ps>pe) return NULL;
    struct TreeNode *root=malloc(sizeof(struct TreeNode));
    root->val=preorder[ps];
    int i=is;
    int j=ps+1;
    if(inorder[ie]==root->val) {
        i=ie;
        j=pe+1;
    } else if (inorder[is]==root->val) {
        j=ps+1;
    } else {
        while(inorder[i]!=root->val) i++;
        while(1){
            int n=1;
            for(int k=is;k<i;k++) {
                if(preorder[j]==inorder[k]) {
                    n=0;
                    break;
                }
            }
            if(n==1) {
                break;
            } else j++;
        }
    }
    root->left=buildTreeHelper(preorder, ps+1, j-1, inorder, is, i-1);
    root->right=buildTreeHelper(preorder, j, pe, inorder, i+1, ie);
    return root;
}
struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    if(preorderSize==0) return NULL;
    return buildTreeHelper(preorder, 0, preorderSize-1, inorder, 0, inorderSize-1);
}
