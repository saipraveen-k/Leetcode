import heapq
class Solution(object):
    def mergeKLists(self, lists):
        min_heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, i, lst))
        dummy = ListNode(0)
        current = dummy
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        return dummy.next