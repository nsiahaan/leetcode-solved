/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    // slow + fast ptr approach
    // slow moves 1 step, fast moves 2 steps -> when fast reaches end, slow should be in the middle
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    
    while (fast && fast->next != NULL) { // while fast ptr (and next pos) isn't null
        fast = fast->next->next;
        slow = slow->next;
    }
    return slow;
}
