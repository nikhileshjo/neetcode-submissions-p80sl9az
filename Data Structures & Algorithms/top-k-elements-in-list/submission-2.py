class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorting
        freq_counter = {}
        for i in nums:
            if i in freq_counter:
                freq_counter[i] += 1
            else:
                freq_counter[i] = 1
        result = []

        for num, cnt in freq_counter.items():
            result.append([cnt, num])
        
        result.sort(reverse = True)
        result_dash = []

        l = 0

        while len(result_dash) < k:
            result_dash.append(result[l][1])
            l += 1
        return result_dash