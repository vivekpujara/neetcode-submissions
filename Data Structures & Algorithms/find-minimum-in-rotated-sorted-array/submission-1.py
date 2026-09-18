class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]  # initialize arbitrary first val
        l, r = 0, len(nums) - 1

        while l <= r:
            # if we get to a portion of the array that's already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # if the array is not sorted, that's when we'll do our binary search portion
            m = (l + r) // 2
            res = min(res, nums[m])  # because we're updating the res w/ mid val, pointers below
                                     # will be +/- from the mid pointer

            # now search to left or right
            if nums[m] >= nums[l]:
                # search right portion
                l = m + 1
            # otherwise search left portion
            else:
                r = m - 1
        
        return res

"""
should we rotate back to normal based on len(nums)? no
then implement binary search? (as the array needs to be sorted, default to ascending)
only unique elements present, which is good

T: O(log N)
S: O(1)

--

# my initial attempt (results in correct solution but does not navigate the array rotation stepwise)


        # need to rotate back, or initialize pointers at the rotation point
        nums = sorted(nums)

        left, right = 0, len(nums) - 1
        mid = len(nums) // 2
        target = min(nums)

        while left < right:
            if target < nums[mid]:
                right = mid
                mid = (right - left) // 2
            elif target < nums[mid]:
                left = mid
                mid = (right - left) // 2
            elif target == nums[mid]:
                return nums[mid]

"""