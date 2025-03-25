class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=defaultdict(list)
        for s in strs:
            sort=''.join(sorted(s))
            r[sort].append(s)
        return list(r.values())
