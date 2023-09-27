# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #Brute force
        # while headA:
        #     ptr = headB
        #     while ptr:
        #         if headA == ptr:
        #             return headA
        #         ptr=ptr.next
        #     headA=headA.next
        # return None

        #Better 
        # s = set()
        # while headA:
        #     s.add(headA)
        #     headA=headA.next
        # while headB:
        #     if headB in s:
        #         return headB
        #     headB=headB.next
        # return None
        #Best
        ptr1=headA
        ptr2=headB
        while ptr1 != ptr2:
            ptr1 = headB if ptr1 is None else ptr1.next
            ptr2 = headA if ptr2 is None else ptr2.next
        return ptr1

        