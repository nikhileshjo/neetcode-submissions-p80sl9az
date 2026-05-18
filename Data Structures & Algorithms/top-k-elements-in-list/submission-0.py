class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            counter[i] = 1 + counter.get(i, 0)
        
        cnts = []

        for num, cnt in counter.items():
            cnts.append([cnt, num])
        
        cnts.sort(reverse=True)

        output = []

        for i in range(k):
            output.append(cnts[i][1])
        
        return output