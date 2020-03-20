#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 单纯的链表操作。。。
        # 但还是容易翻车
        if not head:
            return None
        elif not head.next:
            return head
        first = head
        second = head.next
        tmp = second.next
        head = second
        second.next = first
        first.next = tmp
        if not head.next.next:
            return head
        last = head.next
        first = head.next.next
        second = head.next.next.next
        while second:
            tmp = second.next
            second.next = first
            last.next = second
            first.next = tmp
            if first.next:
                second = first.next.next
                last = first
                first = first.next
            else:
                return head
        return head



# @lc code=end

