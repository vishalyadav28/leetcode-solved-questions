# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Reverse k length linked list
        def reverseNode(head, k):
            prev = None
            current = head

            while k > 0:
                if not current:
                    return None
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1

            return prev, current  # Return both the new head and the next node after the reversed group

        # Get length of linkedlist
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        length = get_length(head)

        if length < k:
            return head

        new_head = None
        prev_tail = None

        while length >= k:
            current_head = head
            tail, head = reverseNode(head, k)  # Retrieve the new tail and the next node after the reversed group
            
            if not tail:
                break

            if not new_head:
                new_head = tail

            if prev_tail:
                prev_tail.next = tail

            prev_tail = current_head
            length -= k

        if prev_tail:
            prev_tail.next = head

        return new_head

