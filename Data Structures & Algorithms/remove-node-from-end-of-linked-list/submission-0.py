# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        leng = 0
        curr = head

        while curr:       
            leng += 1
            curr = curr.next
        
        target = leng - n
        if target == 0:
            return head.next

        count = 0
        curr = head
        while curr:
            if count == target - 1:
                curr.next = curr.next.next
            
            count += 1
            curr = curr.next


        return head
