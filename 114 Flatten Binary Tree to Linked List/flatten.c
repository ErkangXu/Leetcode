/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
  * };
 */
struct TreeNode* flattenHelper(struct TreeNode *root) {
    struct TreeNode *t = root;
    struct TreeNode *r = root->right; // You have to save the right son, otherwise it will be overwritten by t->right=flattenHelper(root->left);
    if(root->left!=NULL){
        t->right=flattenHelper(root->left);
        while(t->right!=NULL) t=t->right;
    }
    root->left=NULL; // Need to clear the left branch of the root
    if(r!=NULL){
        t->right=flattenHelper(r);
    }
    return root;
}
void flatten(struct TreeNode *root) {
    if (root==NULL) return;
    flattenHelper(root);
}