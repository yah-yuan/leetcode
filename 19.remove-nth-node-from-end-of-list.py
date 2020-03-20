#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 维护一个长度为 n+1 的链表的指针头，如果超过n则将该链表头部后移

        r_head = tmp = head
        count = 0
        count_all = 0
        while head:
            if count == n + 1:
                r_head = r_head.next
            else:
                count += 1
            count_all += 1
            head = head.next
        if count_all == 1:
            return None
        # if r_head == tmp and count != count_all and n == 1:
        if n == count_all:
            return tmp.next
        r_head.next = r_head.next.next
        return tmp

        
# @lc code=end

