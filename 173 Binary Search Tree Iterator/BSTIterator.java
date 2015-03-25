/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class BSTIterator {
    private LinkedList<TreeNode> stack;
    TreeNode cur;
    public BSTIterator(TreeNode root) {
        stack = new LinkedList<TreeNode>();  // Using linkedlist as stack
        cur = root;
        while(cur!=null && cur.left!=null) {
            stack.add(cur);  // The method is add not put
            cur=cur.left;
        }
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        if (cur==null) return false;
        return true;
    }

    /** @return the next smallest number */
    public int next() {
        int value = cur.val;
        if(cur.right!=null) {
            cur=cur.right;
            while(cur.left!=null) {
                stack.add(cur);
                cur=cur.left;
            }
        } else if (!stack.isEmpty()){
            cur=stack.pollLast();    // Using those functions to imutate a stack, but it's slower than using ArrayList and pointer
        } else {
            cur=null;
        }
        return value;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */