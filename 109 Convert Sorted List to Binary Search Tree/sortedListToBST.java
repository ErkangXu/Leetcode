/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
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
    public TreeNode sortedListToBST(ListNode head) {
        if(head==null) return null;
        if(head.next==null) {
            return new TreeNode(head.val);
        }  // The following code cannot handle the situation where head is null or a single node, so I need the above code to handle them
        ListNode sr = head;
        ListNode fr = head;
        while(fr.next.next!=null && fr.next.next.next!=null) { // Need to check next pointer layer by layer gradually
            fr=fr.next.next;
            sr=sr.next;
        }
        fr=sr.next.next;
        TreeNode rn = new TreeNode(sr.next.val);
        sr.next=null;
        rn.left=sortedListToBST(head);
        rn.right=sortedListToBST(fr);
        return rn;
    }
}