/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    if(!head) return NULL;
    struct ListNode *fast = head;
    struct ListNode *slow = head;
    while (fast->next && fast->next->next) {
        fast=fast->next->next;
        slow=slow->next;
        if(fast==slow) {
            while(head!=slow) {
                head=head->next;
                slow=slow->next;
            }
            return head;
        }
    }
    return NULL;
}