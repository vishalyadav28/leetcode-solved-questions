# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #extra space O(n) and O(n) time
        s=set()
        temp = head
        while temp:
            if temp in s:
                return True
            else:
                s.add(temp)
            temp=temp.next
        return False
        # time and space => O(n)
        # slow = fast = head
        # while fast and slow and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False
        
        