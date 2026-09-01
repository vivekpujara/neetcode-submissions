class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # while window INVALID (sliding window (exception) criteria, from left)
            # while (window_length - most_freq_char) > k, we want to slide (shrink) from left
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

"""
mind goes to sliding window
all UPPERCASE chars
want highest cluster of same chars, requiring minimal replacements, to achieve longest substring
want to pass over each element once
need a way to reset substring (move left pointer of sliding window)

return len(longest_substring)

T: O(N)
S: O(N) or O(1)

first attempt

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        replacements_needed = 0
        l = 0

        for r in range(len(s)):
            if s[r] == s[l]:
                r += 1
                res += 1
            elif s[r] != s[l]:
                if replacements_needed <= k:
                    replacements_needed += 1
                    res += 1
                else:
                    # move left pointer forward for new substring
                    l += 1
                    # reset repl needed counter
                    replacements_needed = 0
            res = max(res, r - l + 1)

        return res
"""