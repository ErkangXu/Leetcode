/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode forehead = new ListNode(-1);
        forehead.next=head;
        ListNode current = head;
        ListNode nextUniq = head;
        ListNode previous = forehead;
        while(current!=null){
            int dupCounter=0;
            while(nextUniq!=null && nextUniq.val==current.val){
                nextUniq=nextUniq.next;
                dupCounter++;
            }
            if(dupCounter==1){
                previous=current;
            } else previous.next=nextUniq;
            current=nextUniq;
        }
        return forehead.next;
    }
}