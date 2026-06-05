class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting
        anagram_list = {}
        for s in strs:
            s_sort = ''.join(sorted(s))
            if s_sort in anagram_list:
                anagram_list[s_sort].append(s)
            else:
                anagram_list[s_sort] = [s]
        output = []
        for a in anagram_list.values():
            output.append(a)
        return output