#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        overnum = 0
        num1 = 0
        num2 = 0
        new = ListNode(0)
        node = new
        while True:
            if not (l1 or l2):
                if overnum:
                    node.next = ListNode(overnum)
                break
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            res = num1 + num2 + overnum
            overnum = int(res / 10)
            node.next = ListNode(res % 10)
            node = node.next
        return new.next
        
# @lc code=end

