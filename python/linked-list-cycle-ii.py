# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Brute O(n^2)
        fast = slow = head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                slow=head
                while fast!=slow:
                    fast=fast.next
                    slow=slow.next
                return
        #Better O(2n)
        # fast=slow=head
        # while fast and fast.next and slow:
        #     slow = slow.next
        #     fast=fast.next.next
        #     if fast==slow:
        #         break
        # else:
        #     return None
        # pointer = head
        # while pointer != fast:
        #     fast=fast.next
        #     pointer = pointer.next
        # return pointer

        