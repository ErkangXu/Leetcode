/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  struct TreeLinkNode *left, *right, *next;
 * };
 *
 */

void connect(struct TreeLinkNode *root) {
    if(root==NULL || root->left==NULL) return;
    connect(root->right);
    connect(root->left);
    struct TreeLinkNode *l = root->left; // Using local varible is faster than using a global one
    struct TreeLinkNode *r = root->right;
    do{
        l->next=r; // Need to connect at every level
        l=l->right;
        r=r->left;
    }while(l!=NULL); // Need ; to end a do .. while loop
}