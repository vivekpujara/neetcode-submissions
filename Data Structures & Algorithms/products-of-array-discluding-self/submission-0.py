class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. Create our answer list, starting with all 1s
        answer_array = [1] * len(nums)

        # 2. Walk LEFT-TO-RIGHT to collect products of elements on the LEFT (prefix)
        product_of_everything_to_the_left = 1
        for i in range(len(nums)):
            answer_array[i] = product_of_everything_to_the_left
            product_of_everything_to_the_left *= nums[i]
        
        # 3. Walk RIGHT-TO-LEFT to collect products of elements on the RIGHT (suffix or postfix)
        product_of_everything_to_the_right = 1
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the left product (already there) by the right product
            answer_array[i] *= product_of_everything_to_the_right
            product_of_everything_to_the_right *= nums[i]
        
        return answer_array

"""
T: O(n)
We loop through the array of length n twice: once forward (prefix) and once backward (postfix).O(n) + O(n) = O(2n), which simplifies to O(n).

S: O(n)
Auxiliary Space: O(1) because we only use a few variables (prefix, postfix, i) that require constant extra space. Total Space: O(n) solely for the answer_array output array, which the problem requires us to return.
"""