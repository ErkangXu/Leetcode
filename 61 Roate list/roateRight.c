/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *rotateRight(struct ListNode *head, int k) {
    if(!head || !head->next || k==0) return head;
    int c=1; // In corder to keep the last node, need to initialize c as 1
    struct ListNode *lastNode=head;
    while(lastNode->next) {
        lastNode=lastNode->next;
        c++;
    }
    int i=k%c; // k might be very very big, need to calculate the modula
    if(i==0) return head;
    lastNode->next=head; // connect tail to the head
    struct ListNode *f=head;
    for (int j=0;j<c-i-1;j++) f=f->next; // Because we know the length of the list, we don't need to use two pointers actually
    struct ListNode *r=f->next;
    f->next=NULL;
    return r;
}