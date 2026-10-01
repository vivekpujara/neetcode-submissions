class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # state solution/exit condition upfront (most efficient)
            if nums[m] == target:
                return m
            
            # left sorted portion
            elif nums[m] >= nums[l]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1  # going ahead of m because we return m element above
                else:
                    l = m + 1

            # right sorted portion
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        # default if target not present in nums
        return -1


"""
since nums is sorted, and we need to search for target
mind immediately goes to binary search as most efficient algo
for binary search, need l, r, and mid pointers, floor division //
but need to account for rotation of n times, so build it into logic
>= elements likely required for edge cases (like on edges of nums array)
need to find pivot point, then we'll know which way (which section) to search in for target i

T: O(log N)
S: O(1), if store any elements in new array/stack/queue/seen, O(N)?

key insight, to make this as fast and logical as possible,
need to compare target to nums[m], and then to nums[l] and nums[r],
that will help us confirm which sorted portion we're in and has what

first attempt (almost there)

l, r = 0, len(nums) - 1
        m = (r - l) // 2
        res = 0

        while l <= r:
            if nums[m] > nums[m+1]:
                # we've found the pivot point
                if target < nums[m]:
                    # search right section
                    l = m
                    m = (r - l) // 2
                else:
                    # search left section
                    r = m
                    m = (r - 1) // 2

            res = nums[m]
            if res == target:
                return m
            else:
                return -1

    # return 'index pointer at target element' if in nums, else return -1
"""