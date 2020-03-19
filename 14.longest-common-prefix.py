class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        tar = min(strs, key=len)
        strs.remove(tar)
        prefix = ''
        for i in range(len(tar)):
            prefix = tar[:i+1]
            for x in strs:
                if not x.startswith(prefix):
                    return prefix[:-1]
        return prefix