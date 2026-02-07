# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#노드가 []이렇게 표현된다고 리스트가 아님.
#1->2->3->4 이런식임
        visited = set()#노드통째로 저장
        curr=head #첫번째 칸부터 시작

        while curr:#더이상 칸이 없을때까지
            if curr in visited:
                return True

            visited.add(curr)#처음 온칸이면 저장
            curr = curr.next
        return False #끝까지 갓다면 순환이 없다는 뜻
            
        