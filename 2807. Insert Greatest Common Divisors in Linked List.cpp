#include <algorithm>
using namespace std;

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

int gcd(int a, int b)
{
    int result = min(a, b);
    while (result > 0)
    {
        if (a % result == 0 && b % result == 0)
        {
            break;
        }
        result--;
    }
    return result;
}

class Solution
{
public:
    ListNode *insertGreatestCommonDivisors(ListNode *head)
    {
        ListNode *ptr = head;
        while (ptr != nullptr && ptr->next != nullptr)
        {
            int a = ptr->val;
            int b = ptr->next->val;
            int c = gcd(a, b);
            ListNode *new_node = new ListNode(c);
            new_node->next = ptr->next;
            ptr->next = new_node;
            ptr = ptr->next->next;
        }
        return head;
    }
};