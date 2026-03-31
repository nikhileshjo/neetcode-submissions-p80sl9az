class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i in num_set:
            if i - 1 in num_set:
                continue
            else:
                curr = i
                l = 1
                while curr + 1 in num_set:
                    l += 1
                    curr += 1
                longest = max(longest, l)
        return longest