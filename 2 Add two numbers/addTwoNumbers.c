tion for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *result=malloc(sizeof(struct ListNode));
    struct ListNode *rw=result;
    int c=0;
    while(1) { // Only need to meet one of the requirements
        int o1=0;
        if(l1!=NULL) {
            o1=l1->val;
            l1=l1->next;
        }
        int o2=0;
        if(l2!=NULL){
            o2=l2->val;
            l2=l2->next;
        }
        int s=o1+o2+c;
        rw->val=s%10;
        c=s/10;
        if(l1==NULL && l2==NULL && c==0) {
            rw->next=NULL;
            break;
        }
        rw->next=malloc(sizeof(struct ListNode));
        rw=rw->next;
    }
    return result;
}
