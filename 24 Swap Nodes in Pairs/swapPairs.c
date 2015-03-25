/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *swapPairs(struct ListNode *head) {
    if(head == NULL) return head;
    struct ListNode* result = head->next;
    if (result == NULL) return head;
    struct ListNode* p1 = head;
    struct ListNode* p2 = head->next;
    while(p1->next->next != NULL && p2->next->next != NULL){
        struct ListNode* r1 = p1->next->next;
        struct ListNode* r2 = p2->next->next;
        p2->next = p1;
        p1->next = r2;
        p1 = r1;
        p2 = r2;
    }
    if(p1->next->next) {
        p1->next=p1->next->next;
    } else {
        p1->next = NULL;
    }
    p2->next = p1;
    return result;
}