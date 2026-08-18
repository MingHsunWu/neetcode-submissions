class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = s.lower()
        s_list = [i for i in s_ if i != ' ']
        l, r = 0, len(s_list) -1
        while l < r:
            while l < r and not (ord('A') <= ord(s_list[l]) <= ord('Z') or ord('a') <= ord(s_list[l]) <= ord('z')or ord('0') <= ord(s_list[l]) <= ord('9')):
                l += 1
            while r > l and not (ord('A') <= ord(s_list[r]) <= ord('Z') or ord('a') <= ord(s_list[r]) <= ord('z')or ord('0') <= ord(s_list[r]) <= ord('9')):
                r -= 1
            if s_list[l] != s_list[r]:
                return False
            l += 1
            r -= 1
        return True