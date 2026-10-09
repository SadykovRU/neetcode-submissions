class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup_map = dict()

        for s in strs:
            if tuple(sorted(s)) in lookup_map:
                lookup_map[tuple(sorted(s))].append(s)
            else:
                lookup_map[tuple(sorted(s))] = [s]
        
        output = []
        for v in lookup_map.values():
            output.append(v)
        
        return output
