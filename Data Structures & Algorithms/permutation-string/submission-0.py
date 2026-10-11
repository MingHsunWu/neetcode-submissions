class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w_length = len(s1)
        if w_length > len(s2):
            return False
        
        s1_dic = {}
        s2_dic = {}
        for s in range(w_length):
            s1_dic[s1[s]] = 1 + s1_dic.get(s1[s], 0)
            s2_dic[s2[s]] = 1 + s2_dic.get(s2[s], 0)
        if s1_dic == s2_dic:
            return True
             
        l = 0
        for r in range(w_length, len(s2)):
            s2_dic[s2[r-w_length]] -= 1
            s2_dic[s2[r]] = 1 + s2_dic.get(s2[r], 0)
            if s2_dic.get(s2[r-w_length], 0) == 0:
                s2_dic.pop(s2[r-w_length])

            if s1_dic == s2_dic:
                return True
        print(s1_dic)
        print(s2_dic)
        return False






