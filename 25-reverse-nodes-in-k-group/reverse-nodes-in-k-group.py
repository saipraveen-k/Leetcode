class Solution(object):
    def reverseKGroup(self, head, k):
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        new_head = self.reverse(head, curr)
        head.next = self.reverseKGroup(curr, k)
        return new_head
    
    def reverse(self, head, stop):
        prev = None
        while head != stop:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev