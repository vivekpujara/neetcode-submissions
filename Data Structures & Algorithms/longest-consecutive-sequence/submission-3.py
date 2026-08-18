class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for n in num_set:
            if (n - 1) not in num_set:  # check if start of sequence
                length = 1
                while (n + length) in num_set:
                    length += 1
                max_len = max(max_len, length)
        
        return max_len

"""
maybe sort first? sorted(nums) returns a new list which is the correct way to avoid returning None for a TypeError
can have duplicate elements, and still have ongoing sequence, use set?
indiv elements in nums can be negative, so soln must solve this edge case as well
deal with broken sequences (need to reset upon true broken sequence, then compare length of the collected sequences, and then just return the len of the one with the max length. for this hash set might be best)
consider all edge cases and variants of the nums input array, does our algo handle all?

return len of longest up-by-1 consecutive sequence

T: must be O(n) - just iterate over array once? sorting might add time to make it O(NlogN)
S: at least O(n)? - for creating an additional array to hold the longest consec seq
    if there's an in-place method to do this, then maybe O(1) space, but we'll see

# my orig solution (did not handle edge cases)

    longest_consec_seq = []
            # sorted_nums = nums.sort()
            for num in sorted(nums):
                if not longest_consec_seq:
                    longest_consec_seq.append(num)
                if longest_consec_seq[-1] == (num-1):
                    longest_consec_seq.append(num)
        
            return len(longest_consec_seq)

# T O(NlogN) sort solution

if not nums:
            return 0
        
        sorted_nums = sorted(list(set(nums)))

        max_len = 1
        curr_len = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                curr_len += 1
            else:
                curr_len = 1  # reset streak
            max_len = max(max_len, curr_len)
        
        return max_len
"""