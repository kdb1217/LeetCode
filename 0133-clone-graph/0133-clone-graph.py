

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        clones = {node: Node(node.val)}  
        queue = deque([node])

        while queue:
            cur = queue.popleft()

            for i in cur.neighbors:
                if i not in clones:
                    clones[i] = Node(i.val)
                    queue.append(i)
                clones[cur].neighbors.append(clones[i])
        return clones[node]

    


        