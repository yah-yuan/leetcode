#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        # 行不通,在"aaaaaaaa",["aa","aa","aa"]的情况下,应该要借助map
        # 边界条件太多了!
        # 也可能是我算法太垃圾,换map试试,先把所有map遍历出来?只有O(n^2)的复杂度
        # "wordgoodgoodgoodbestword"\n["word","good","best","word"]
        start = 0
        s_length = len(s)
        if s_length == 0:
            return []
        l_length = len(words)
        if l_length == 0:
            return []
        w_length = len(words[0])
        if w_length == 0:
            return list(range(s_length+1))
        end = w_length
        res = []
        while end<=s_length:
            # print(start,end)
            while s[start:end] not in words:
                # 找到开始字符串
                start += 1
                end += 1
                if end>s_length:
                    return res
            queue = []
            o_index = start
            index = start
            while end <= s_length:
                word = s[start:end]
                print(index,start,end,word,queue)
                if len(queue) == l_length:
                    if index not in res:
                        res.append(index)
                    if word != queue[0]:
                        words = queue
                        break
                    else:
                        start += w_length
                        end += w_length
                        index += w_length
                        queue.append(queue.pop(0))
                elif word in words:
                    queue.append(word)
                    words.remove(word)
                    start += w_length
                    end += w_length
                elif word in queue:
                    while queue:
                        tmp = queue[0]
                        if tmp != word:
                            index += w_length
                            # 回收
                            words.append(queue.pop(0))
                        else:
                            queue.append(queue.pop(0))
                            start += w_length
                            end += w_length
                            index += w_length
                            break
                    if not queue:
                        break
                else:
                    words += queue
                    break
            # print(o_index)
            start = o_index + 1
            end = o_index + w_length + 1
            if len(words) == 0:
                words = queue
                if index not in res:
                    res.append(index)
        return res
            
# @lc code=end

s = Solution()
print(s.findSubstring("aaaaaaaa",["aa","aa","aa"]),[0,1,2])
# print(s.findSubstring("barfoothefoobarman",["foo","bar"]),[0,9])
# print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]),[8])
# print(s.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]),[6,9,12])
# print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"]),[])
# print(s.findSubstring("bfbthefoobarman",["f","b"]),[0,1])
# print(s.findSubstring("bfbfbfthefoobarman",["f","b"]),[0, 1,2, 3, 4])
