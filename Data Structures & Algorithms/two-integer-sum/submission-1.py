class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_set = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in n_set:
                return [n_set[diff], i]
            else:
                n_set[n] = i
