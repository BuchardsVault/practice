

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        remaining = {}

        for ch in s:
            remaining[ch] = remaining.get(ch,0) + 1
        for ch in t:
            if ch not in remaining:
                return False
            remaining[ch] -= 1
            if remaining[ch] == 0:
                del remaining[ch]

        return len(remaining) == 0

        


