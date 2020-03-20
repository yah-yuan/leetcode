#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 链表的基本操作，主要是临界条件需要注意
        if l1 and l2:
            if l1.val <= l2.val:
                res = l1
                merged = l2
            else:
                res = l2
                merged = l1
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None
        # 以上，解决谁作为返回谁被合并
        head = res
        while True:
            if not head.next:
                head.next = merged
                break
            if not merged:
                break
            if head.next.val < merged.val:
                head = head.next
                continue
            else:
                tmp = merged.next
                merged.next = head.next
                head.next = merged
                merged = tmp
                head = head.next
        return res

# @lc code=end

