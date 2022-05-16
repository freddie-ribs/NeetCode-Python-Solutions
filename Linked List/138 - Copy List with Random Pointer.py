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
        '''
        Time: O(n), really 2n, since two passes, but it simplyfies to n
        Space: O(n)
        '''
        d = {None: None}

        m = n = head

        while m:
            d[m] = Node(m.val)
            m = m.next

        while n:
            copy = d[n]
            copy.next = d[n.next]
            copy.random = d[n.random]
            n = n.next

        return d[head]
