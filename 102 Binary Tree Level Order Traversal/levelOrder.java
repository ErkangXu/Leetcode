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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>(); // Can only implement layer by layer
        if(root==null) return result;
        ArrayList<TreeNode> pool = new ArrayList<TreeNode>();
        pool.add(root);
        while(!pool.isEmpty()) { // Forgot the ()
            ArrayList<TreeNode> next = new ArrayList<TreeNode>();
            List<Integer> tmp = new ArrayList<Integer>();
            for(TreeNode t:pool){
                tmp.add(t.val);
                if(t.left!=null) next.add(t.left);
                if(t.right!=null) next.add(t.right);
            }
            result.add(tmp);
            pool=next;
        }
        return result;
    }
}