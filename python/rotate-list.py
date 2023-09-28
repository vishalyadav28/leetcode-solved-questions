# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(head):
            
            length = 1
            temp=head
            while temp.next != None:
                length+=1
                temp=temp.next
            return length,temp

        if head == None or head.next == None:
            return head
        #get length
        length,last_node = get_length(head)


        #connect last to first
        last_node.next = head
        k%=length
        end = length - k
        while end:
            last_node = last_node.next
            end-=1
        
        head = last_node.next
        last_node.next = None
        return head

            

        