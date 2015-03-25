/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *partition(struct ListNode *head, int x) {
    if(head==NULL) return NULL;
    if(head->next==NULL) return head;
    struct ListNode preo;
    struct ListNode* pre=&preo;
    pre->next=head;
    struct ListNode* ph = pre;
    struct ListNode* back;
    while(pre->next!=NULL && pre->next->val<x){
        pre=pre->next; // I used pre++ here before, what a joke!
    }
    if (pre->next==NULL) return ph->next;
    back=pre->next;
    struct ListNode* kf=back;
    while(back!=NULL){
        while(back->next!=NULL && back->next->val>=x) back=back->next;
        if (back->next==NULL) break;
        pre->next=back->next;
        pre=pre->next;
        back->next=back->next->next;
        //back=back->next; This is wrong, should move the "back" pointer in the last while loop
    }
    pre->next=kf;
    return ph->next;
}