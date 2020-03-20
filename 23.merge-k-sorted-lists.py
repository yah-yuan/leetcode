#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 我的解法1，直接使用之前的mergetwo，有很多无用的遍历
        length = len(lists)
        if length == 0:
            return None
        if length == 1:
            return lists[0]
        res = lists[0]
        for i in range(len(lists)-1):
            res = self.mergeTwoLists(res, lists[i+1])
        return res

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # divid-and-conquer
        # 二分法， 直到我们能解决的 merge2 问题
        length = len(lists)
        if length == 0:
            return None
        elif length == 1:
            return lists[0]
        else:
            div = int(length/2)
            l1 = self.mergeKLists(lists[0:div])
            l2 = self.mergeKLists(lists[div:])
            return self.mergeTwoLists(l1, l2)
        
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

