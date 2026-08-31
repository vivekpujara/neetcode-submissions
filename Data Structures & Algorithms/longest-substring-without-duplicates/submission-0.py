class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, len(char_set))  # r - l + 1 can also be represented by len(char_set)
        
        return res


"""
return LENGTH of longest substring
NO duplicate chars
substring is contig (serial) seq of chars
maybe algo hinges on detecting when there's a repeating char
then terminate current substring, and start new one

brute force
store substrings

optimized
sort? duplicates would be next to each other
but does that break the string contraint?
in-place? two pointers --> sliding window
could just use if block to compare ord(char) vals from the sliding window pointers
if same (duplicate) ASCII val, terminate substring
hashmap dict (len:substring)


T: O(N)
S: O(N)

first attempt

# longest_substring = []
        l, r = 0, 1
        longest_seen_substring = 0
        len_current_substring = 0
        
        while l < r and r <= len(s) - 1:
            ascii_left = ord(s[l])
            ascii_right = ord(s[r])
            if ascii_left != ascii_right:
                longest_seen_substring += 1
                len_current_substring += 1
                r += 1
            elif ascii_left == ascii_right:
                r += 1
                l = r - 1
                len_current_substring = 0
        
        return max(longest_seen_substring, len_current_substring)
"""