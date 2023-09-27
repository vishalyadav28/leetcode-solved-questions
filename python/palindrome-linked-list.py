# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #BruteForce
        # slow = fast = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast:
        #         slow=slow.next
        # def reverse(head):
        #     current = head
        #     prev=None
        #     while current:
        #         next = current.next
        #         current.next = prev
        #         prev = current
        #         current = next
        #     return prev
        # head2 = reverse(slow)
        # while head2:
        #     if head.val!=head2.val:
        #         return False
        #     head=head.next
        #     head2=head2.next
        # return True
        #Better
        slow=fast=head
        rev=None
        while fast and fast.next:
            fast=fast.next.next
            temp=rev
            rev=slow
            slow=slow.next
            rev.next = temp
        if fast:
            slow = slow.next
        while rev:
            if rev.val != slow.val:
                return False
            rev =  rev.next
            slow = slow.next
        return True



        