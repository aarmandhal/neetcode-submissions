class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)

        letters = set(s)
        letters |= set(t)

        for k in letters:
            if a[k] != b[k]:
                return False
        
        return True