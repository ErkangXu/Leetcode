/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode sortList(ListNode head) {
        if(head==null || head.next==null) return head;
        ListNode fp=head;
        ListNode sp=head;
        while(fp.next!=null && fp.next.next!=null) {
            fp=fp.next.next;
            sp=sp.next;
        }
        fp=sp.next;
        sp.next=null;
        ListNode l=sortList(head);
        ListNode r=sortList(fp);
        ListNode ns= new ListNode(-1);
        ListNode nss=ns;
        while(l!=null && r!=null) {
            if(l.val<r.val) {
                ns.next=l;
                l=l.next;
            } else {
                ns.next=r;
                r=r.next;
            }
            ns=ns.next;
        }
        ns.next= (l==null)? r:l;
        return nss.next;
    }
}