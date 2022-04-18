# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = self.length(head)
        if l == 0 or l == 1:
            return True
        arr = self.toarray(head)
        left = 0
        right = l - 1
        while right > left:
            if arr[left] != arr[right]:
                return False
            left +=1
            right -=1
            
        return True  

    def access(self, head, n):
        for _ in range(n-1):
            head = head.next
        return head.val
    def length(self, head):
        count = 0
        while head:
            count +=1
            head = head.next
        return count
    
    def toarray(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr