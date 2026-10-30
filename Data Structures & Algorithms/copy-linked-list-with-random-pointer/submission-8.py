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

        mydict = {None: None}
        node = head 
        while node:
            mydict[node] = Node(node.val)
            node = node.next

        node = head 
        while node:
            mydict[node].next = mydict[node.next]
            mydict[node].random = mydict[node.random]
            node = node.next

        return mydict[head]
        