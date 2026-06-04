class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash maps
        exists = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in exists:
                return [exists[x], i]
            else:
                exists[nums[i]] = i
        return []