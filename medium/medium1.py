# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        preserve= ""
        count = 0
        left = right = 0
        while right <= len(s)-1:
            if s[right] not in preserve:
                preserve += s[right]
                count = max(len(preserve) , count)
            else:
                index_in_preserve = preserve.index(s[right])
                preserve = preserve[index_in_preserve + 1:]
                preserve += s[right]
                left += index_in_preserve + 1
            right += 1
        return count

def isPalindrome(s):
    return s == s[::-1]

sol = Solution()
result = sol.lengthOfLongestSubstring("c")
print(result)