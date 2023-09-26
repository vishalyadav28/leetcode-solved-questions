# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummylist = ListNode(0)
        p1,p2= list1,list2
        tail = dummylist
        while True:
            if p1 is None:
                tail.next = p2
                break
            if p2 is None:
                tail.next = p1
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        return dummylist.next
