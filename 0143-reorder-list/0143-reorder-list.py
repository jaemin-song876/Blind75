# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #1. find the middle component

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #2. slow is in the middle, slow.next is hind part
        hind = slow.next
        slow.next = None

        prev = None
        while hind:
            tmp = hind.next
            hind.next = prev
            prev = hind# "hind가 가리키는 노드를 prev도 같이 가리켜"
            hind = tmp
        #3. merge
        front = head

        while prev:
            tmp1 = front.next
            tmp2 = prev.next

            front.next = prev
            prev.next = tmp1

            front = tmp1
            prev = tmp2

