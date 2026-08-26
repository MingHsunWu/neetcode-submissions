class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_num = 0
        right_num = len(nums) - 1
        mid_num = (left_num + right_num) // 2
        while left_num <= right_num:
            if nums[left_num] == target:
                return left_num
            if nums[right_num] == target:
                return right_num

            if nums[mid_num] == target:
                return mid_num
            elif nums[mid_num] < target:
                left_num = mid_num + 1
            elif nums[mid_num] > target:
                right_num = mid_num - 1

            mid_num = (left_num + right_num) // 2
        return -1