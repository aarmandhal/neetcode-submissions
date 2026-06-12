class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        positions = {}
        strs.sort()
        for n in strs:
            if ''.join(sorted(n)) in positions:
                positions[''.join(sorted(n))].append(n)
            else:
                positions[''.join(sorted(n))] = [n]

        for v in positions.values():
            anagrams.append(v)
        
        return anagrams
            
         