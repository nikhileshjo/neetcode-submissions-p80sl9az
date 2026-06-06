class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        freq_counter = [[] for i in range(len(nums)+1)]
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        for num, cnt in freq_dict.items():
            freq_counter[cnt].append(num)
        result = []
        for i in freq_counter[::-1]:
            for j in i:
                result.append(j)
                if len(result) == k:
                    return result