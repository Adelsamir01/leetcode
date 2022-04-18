# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        ahead = head
        length = self.find_len(head)
        if length == 0:
            return head
        if length == 1 or length == n:
            head = head.next
            return head
        
        for i in range(n):
            ahead = ahead.next
            
        print ahead.val
        while ahead:
            prev = current
            current = current.next
            after = current.next
            ahead = ahead.next
            
        print(current.val)
        current.next = None
        prev.next = after
        return head
        
    def find_len(self, head):
        current = head
        count = 0
        while current:
            count +=1
            current = current.next
        return count