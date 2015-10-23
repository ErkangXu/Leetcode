/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  struct TreeLinkNode *left, *right, *next;
 * };
 *
 */
void connect(struct TreeLinkNode *root) {
    struct TreeLinkNode* levelHead= root;
    struct TreeLinkNode* newH=malloc(sizeof(struct TreeLinkNode));
    while (levelHead){
        newH->next=NULL; //Need to assign NULL to next to break the residue of last loop
        struct TreeLinkNode* connector=newH;
        while(levelHead){
            if (levelHead->left) {
                connector->next=levelHead->left;
                connector=connector->next;
            }
            if (levelHead->right){
                connector->next=levelHead->right;
                connector=connector->next;
            }
            levelHead=levelHead->next;
        }
        levelHead=newH->next;
    }
}