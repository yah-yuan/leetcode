#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

#以下实现了一个自动生成的链表，方便调试
class ListNode(object):
    def __init__(self, l:list):
        self.val = l.pop(0)
        if not l:
            self.next = None
        else:
            self.next = ListNode(l)
    
    def __str__(self):
        # 递归输出,方便调试
        s = str(self.val)
        if not self.next:
            return s
        return '%s %s'%(s, str(self.next))

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 指的是全部倒过来而不是颠倒首尾, 这个版本只颠倒了首尾
        if not head:
            return None
        if k == 1:
            return head
        count = 1
        start = head
        start_last = None
        pointer = head
        pointer_last = None
        while True:
            if not pointer:
                break
            # print(start.val, pointer.val)
            if count == k:
                if not start_last:
                    # 第一次交换时的情况
                    head = pointer
                else:
                    start_last.next = pointer
                # k ==2 是会出现特殊情况， start和pointer互换时
                tmp = pointer.next
                if start.next == pointer:
                    pointer.next = start
                    # 此时 pointer_last==start, 故会陷入start.next=start的死循环
                else:
                    pointer.next = start.next
                    pointer_last.next = start
                start.next = tmp

                count = 1
                start_last = start
                start = start.next
                pointer_last = start_last
                pointer = start
            else:
                count += 1
                pointer_last = pointer
                pointer = pointer.next
        return head
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 指的是全部倒过来的版本,认真读题
        # 时间复杂度: n 为链表长度
        #     time: O(n+(n/k)(k/2)) = O(n^2)
        #     space: O(k)
        if not head:
            return None
        if k == 1:
            return head
        count = 1
        start = head
        start_last = None
        pointer = head
        stack = [] # 这里事实上最多要用O(k)的空间，没满足题目要求，但是如何回溯到前一个节点呢？
        while True:
            if not pointer:
                break
            # print(start.val, pointer.val)
            if count == k:
                reverse_end = start
                left = start
                left_last = start_last
                right = pointer
                right_last = stack.pop()
                while True:
                    if not left_last:
                        # 第一次交换时的情况
                        head = right
                    else:
                        left_last.next = right
                    tmp = right.next
                    if right == left:
                        break
                    elif left.next == right:
                        right.next = left
                        left.next = tmp
                        break
                    else:
                        right.next = left.next
                        right_last.next = left
                        left.next = tmp
                    left_last = right
                    left = right.next
                    right = right_last
                    right_last = stack.pop()

                start_last = reverse_end
                start = reverse_end.next
                pointer_last = reverse_end
                pointer = reverse_end.next
                count = 1
                stack = []
            else:
                count += 1
                stack.append(pointer)
                pointer = pointer.next
        return head


# @lc code=end

s = Solution()
l = ListNode([1,2,3,4,5,6,7,8,9])
res = s.reverseKGroup(l, 4)
print(res)