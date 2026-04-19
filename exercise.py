class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = s.split()
        n = t.split()
        if set(m) == set(n):
            return True
        return False