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
    public void reorderList(ListNode head) {
        if(head==null || head.next==null || head.next.next==null) return;
        ListNode fast=head;
        ListNode slow=head;
        ListNode first=head;
        int count=0;
        while(fast.next!=null && fast.next.next!=null){ // I used == instead of != at first, I used one less "next" 
            fast=fast.next.next;
            slow=slow.next;
            count++;
        }
        ListNode pres = new ListNode(0);
        pres.next=slow;
        slow=slow.next;
        ListNode tmp;
        while(slow!=null){
            tmp=slow.next;
            slow.next=pres.next;
            pres.next=slow;
            slow=tmp;
        }
        ListNode second = pres.next;
        ListNode tmp2;
        for(int i=0;i<count;i++){ // count is half of the length of the list, we only need to loop that many times
            tmp=first.next;
            tmp2=second.next;
            first.next=second;
            first=tmp;
            second.next=first;
            second=tmp2;
        }
        second.next=null; // We need to cut the list down, other wise it's a infinite loop to print
    }
}