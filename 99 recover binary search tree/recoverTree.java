/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    TreeNode first;
    TreeNode firstNext;
    TreeNode second;
    TreeNode previous=new TreeNode(Integer.MIN_VALUE);
    public void recoverTree(TreeNode root) {
        recoverTreeHelper(root);
        if (second==null) second=firstNext;
        int tmp=first.val;
        first.val=second.val;
        second.val=tmp;
    }
    public void recoverTreeHelper(TreeNode root){
        if (root==null || second!=null) return; // Change the sequence of the judgement can improve speed
        recoverTreeHelper(root.left);
        if (root.val<previous.val) {
            if (first==null) {
                first=previous;
                firstNext=root;
            } else second=root;
        } 
        previous=root;
        recoverTreeHelper(root.right);
    }
}