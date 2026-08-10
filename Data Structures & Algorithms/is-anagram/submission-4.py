class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_ = set(s)
            for i in s_:
                a = 0
                a = a + s.count(i)
                a = a - t.count(i)
                if a != 0:
                    return False
            return True