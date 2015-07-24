/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void sumHelper(struct TreeNode* root, int target, int position, int* holder, int** result, int* columnSizes, int* returnSize) {
    if (root==NULL) return;
    int rootVal=root->val;
    holder[position]=rootVal;
    if(rootVal==target && root->left==NULL && root->right==NULL) { /* Should be root to leaf path, can't stop in the middle */
        int* seq=(int*)malloc((position+1)*sizeof(int)); /* Only allocate memory when we find a sequence, reuse the holder */
        for(int i=0; i<=position; i++) seq[i]=holder[i];
        result[*returnSize]=seq;
        columnSizes[*returnSize]=position+1;
        (*returnSize)++; /* must bracket the dereference */
        return; /* can end here to save some time */
    }
    sumHelper(root->left, target-rootVal, position+1, holder, result, columnSizes, returnSize);
    sumHelper(root->right, target-rootVal, position+1, holder, result, columnSizes, returnSize);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** pathSum(struct TreeNode* root, int sum, int** columnSizes, int* returnSize) {
    int** result=(int**)malloc(1000*sizeof(int*)); /* Need to cast the pointer*/
    *columnSizes=(int*)malloc(1000*sizeof(int)); /* Need to cast the pointer*/
    int* holder=(int*)malloc(1000*sizeof(int)); /* Need to cast the pointer*/
    *returnSize=0;
    sumHelper(root, sum, 0, holder, result, *columnSizes, returnSize); /* can't use gloabl variable */
    return result;
}
