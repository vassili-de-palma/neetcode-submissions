# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2
        node = dummy = ListNode()
        carry = 0
        while node1 or node2:
            v1 = 0 if not node1 else node1.val
            v2 = 0 if not node2 else node2.val
            digitsum = v1 + v2
            node.next = ListNode( (carry + digitsum) % 10 )
            carry = 1 if carry + digitsum >= 10 else 0
            node1 = None if not node1 else node1.next
            node2 = None if not node2 else node2.next
            node = node.next
        node.next = ListNode(1) if carry == 1 else None
        return dummy.next
            

            




        