class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1  # as these pointers are indices
            while l < r:
                three_sum = val + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res


"""
returned triplet combinations must be unique
return in any order, so don't need to sort? maybe sorting would make it more efficient though
maybe two pointers or sliding window? two pointers may be more appropriate
once triplet_counter gets to 3, eval if triplets == 0, if yes, append triplet, then reset
handle zeros

T: O(N^2)?
S: O(1) or O(N) depending on sorting algo/library function

"""