class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = Counter(t) - Counter(s)
        return list(d.keys())[0]