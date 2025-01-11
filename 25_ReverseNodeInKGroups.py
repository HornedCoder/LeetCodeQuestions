'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if we have atleast K nodes left.
        def hasKNodes(node, k):
            count = 0
            while node and count < k:
                count += 1
                node = node.next
            return count == k
        
        #Helper Function for reversing the LL.
        def reverseGroup(head, k):
            prev = None
            curr = head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev, head
        
        #If empty list or k=1 no need to reverse.
        if not head or k == 1:
             return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while head:
            # If we don't have k nodes left, keep remaining nodes as is
            if not hasKNodes(head, k):
                break
            
            # The current groups last node will be head
            next_group = head
            for _ in range(k-1):
                next_group = next_group.next
            
            # Save the next group start
            next_start = next_group.next

            # Reverse Current Group
            new_head, new_tail = reverseGroup(head, k)

            # Connect with previous group
            prev_group.next = new_head

            # Connect with next group
            new_tail.next = next_start

            # Move pointer
            prev_group, head = new_tail, next_start

        return dummy.next
