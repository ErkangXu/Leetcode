/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public static List<Integer> inorderTraversalList;
    public boolean isValidBST(TreeNode root) {
        if(root==null) return true;
        inorderTraversalList = new ArrayList<Integer>(); // You can't initialize it out side;
        traverse(root);
        int size=inorderTraversalList.size();
        if (size==1) return true;
        for(int i=1;i<size;i++){
            if(inorderTraversalList.get(i-1)>=inorderTraversalList.get(i)) return false; // Used i-0 here before
        }
        return true;
    }
    void traverse(TreeNode root) {
        if (root==null) return;
        traverse(root.left);
        inorderTraversalList.add(root.val);
        traverse(root.right);
    }
}