# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # point p1 to list1 head
        p1=list1
        # point p2 to list2 head
        p2=list2
        # create a dummy node 
        dummy_node = ListNode(0)
        tail = dummy_node
        while True:
            if p1 is None: 
                tail.next = p2
                break
            if p2 is None:
                tail.next = p1
                break
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail=tail.next
        # as head is 0 that's why return dummy_node.next
        return dummy_node.next
