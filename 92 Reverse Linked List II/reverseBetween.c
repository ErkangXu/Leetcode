/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *reverseBetween(struct ListNode *head, int m, int n) {
    if(!head) return head;
    if(m==n) return head;
    struct ListNode* b = head;
    struct ListNode fh;
    if(m==1) {
        fh.next=head;
        b=&fh;
    } else {
        int i=0;
        while(b->next!=NULL && i<m-2){
            b=b->next;
            i++;
        }
        if (i!=m-2) return head;
    }

    int j = 0;
    struct ListNode* f=b->next;
    struct ListNode* stack[n-m+1];
    int p=-1;

    while(f!=NULL && j<n-m+1){
        stack[++p]=f;
        f=f->next;
        j++;
    }
    for(int i=0;i<n-m+1;i++){
        b->next=stack[p--];
        b=b->next;
    }
    b->next=f;
    return (m==1)? fh.next:head;
}