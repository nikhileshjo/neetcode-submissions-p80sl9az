class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash maps
        anagram_dict = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ ord(c) - ord('a') ] += 1
            count = tuple(count)
            if count in anagram_dict:
                anagram_dict[count].append(s)
            else:
                anagram_dict[count] = [s]
        output = []
        for a in anagram_dict.values():
            output.append(a)
        return output