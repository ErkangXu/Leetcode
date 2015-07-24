/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int** result;
int currentPosition;
int* sizes;
int* holder;

void sumHelper(struct TreeNode* root, int target, int position) {
    if (root==NULL) return;
    int rootVal=root->val;
    holder[position]=rootVal;
    if(rootVal==target && root->left==NULL && root->right==NULL) { /* Should be root to leaf path, can't stop in the middle */
        result[currentPosition]=(int*)malloc((position+1)*sizeof(int)); /* Only allocate memory when we find a sequence, reuse the holder */
        for(int i=0; i<=position; i++) result[currentPosition][i]=holder[i];
        sizes[currentPosition++]=position+1;
        return; /* can end here to save some time */
    }
    sumHelper(root->left, target-rootVal, position+1);
    sumHelper(root->right, target-rootVal, position+1);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** pathSum(struct TreeNode* root, int sum, int** columnSizes, int* returnSize) {
    result=(int**)malloc(1000*sizeof(int*)); /* Need to cast the pointer*/
    *columnSizes=(int*)malloc(1000*sizeof(int)); /* Need to cast the pointer*/
    sizes=*columnSizes;
    holder=(int*)malloc(1000*sizeof(int)); /* Need to cast the pointer*/
    currentPosition=0; //!!!!! It's crutial to reset the currentPosition, in the stem function
    sumHelper(root, sum, 0);
    *returnSize=currentPosition;
    return result;
}