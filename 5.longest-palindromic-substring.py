class Solution:
    def longestPalindrome(self, s: str) -> str:
        def common_substring(s):
            # reverse中的相同子串
            def get_reverse(s):
                res = ""
                for i in s:
                    res = i + res
                return res
            
            rev_s = get_reverse(s)
            length = len(s)
            if length == 0:
                return ""
            for i in range(length, 0, -1):
                for j in range(0, length - i + 1):
                    if rev_s[0 + j: i + j] == s[length - (i + j): length - j]:
                        return rev_s[0 + j: i + j]
            return s[0]
        def center_expand(s):
            # 中心扩展
            length = len(s)
            if length == 0:
                return ""
            longest = 1
            longest_parli = s[0]
            for i in range(length):
                k = 1
                while k <= i and i+k < length and s[i-k] == s[i+k]:
                    this_length = 2 * k + 1
                    if this_length > longest:
                        longest = this_length
                        longest_parli = s[i-k:i+k+1]
                    k += 1
            for i in range(length - 1):
                k = 0
                while k <= i and i+1+k < length and s[i-k] == s[i+1+k]:
                    this_length = 2 * k + 2
                    if this_length > longest:
                        longest = this_length
                        longest_parli = s[i-k:i+k+2]
                    k += 1
            return longest_parli
        # return common_substring(s)
        return center_expand(s)