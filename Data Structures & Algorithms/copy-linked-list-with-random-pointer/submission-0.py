"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return 

        mp = {}
        curr = head

        while curr:
            copyN = Node(curr.val)
            mp[curr] = copyN

            curr = curr.next
        
        curr = head
        while curr:
            copyN = mp[curr]
            copyN.next = mp.get(curr.next, None)
            copyN.random = mp.get(curr.random, None)

            curr = curr.next
        
        return mp[head]

   


        