class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup_map = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))

            lookup_map[key].append(s)
        
        return list(lookup_map.values())
