class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f_mut = nums.copy()
        b_mut = nums.copy()
        ans = nums.copy()
        i = 1
        while i < len(nums):
            f_mut[i] = f_mut[i-1] * f_mut[i]
            b_mut[-1-i] = b_mut[-1-i] * b_mut[-i]
            i += 1
        ans[0] = b_mut[1]
        ans[-1] = f_mut[-2]
        j = 1
        while j < len(nums)-1:
            ans[j] = f_mut[j-1] * b_mut[j+1]
            j += 1
        
        return ans