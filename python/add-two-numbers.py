# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            _sum = x + y + carry
            carry = _sum // 10
            
            current.next = ListNode(_sum % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy_head.next
        