class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            # condition triggering sliding window
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

"""
all chars in t must be in s to be able to return shortest substring
if not all in there, then return ""

opt
sliding window, L/R
store ASCII t vals in dict?
counter?
return min(seen_substrings)

T: O(N+M)?
S: O(N)?

first attempt

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seensub = []
        l = 0
        res = 0

        for r in range(len(s)):
            for c in t:
                if c != s[r]:  # need to revisit
                    l += 1
                    r += 1
                if c == s[r]:
                    seensub.append(s[r])
                    r += 1
            res = min(res, r - l + 1)
            if res == 0:
                return ""
        return res
"""