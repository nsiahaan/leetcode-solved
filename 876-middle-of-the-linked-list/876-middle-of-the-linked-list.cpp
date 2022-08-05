/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        // traverse the list to count number of nodes
        int counter = 1;
        ListNode* ptr = head;
        
        while (ptr->next != NULL) {
            counter++;
            ptr = ptr->next;
        }
        
        // traverse to n/2th node
        int mid = (counter / 2) + 1;        
        ptr = head;
        for (int i = 1; i < mid; i++) {
            ptr = ptr->next;
        }
        
        return ptr;
    }
};