"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_map ={}

        def dfs(current_node):
            
            if current_node in cloned_map:
                return cloned_map[current_node]
            #첨보는 노드라면??
            #일단 껍데기(값)만 복사해서 새로 만들기
            copy = Node(current_node.val)
            #이제 복사 시작했다고 기록장에 등록
            cloned_map[current_node] = copy

            #이웃들도 복사하기
            for neighbor in current_node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy
        return dfs(node)