# coding:utf-8
# import uuid


class Solution:
    def lengthOfLongestSubstring(self, s):
        lastRepeating = -1
        longestSubstring = 0
        positions = {}
        for i in range(len(s)):
            if s[i] in positions and lastRepeating < positions[s[i]]:
                lastRepeating = positions[s[i]]
            if i - lastRepeating > longestSubstring:
                longestSubstring = i - lastRepeating
            positions[s[i]] = i
        return longestSubstring


if __name__ == "__main__":
    string = 'wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxs\
        jybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'
    solu = Solution()
    length = solu.lengthOfLongestSubstring(string)

    print length
