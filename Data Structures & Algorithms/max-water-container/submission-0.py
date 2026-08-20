class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            res = max(res, area)  # compare prev area vs curr area, and take max

            # now we want to move the pointer inward that is pointing to the lower height
            if heights[l] < heights[r]:
                l += 1  # want to keep the higher height as is (move the other one)
            else:
                r -= 1
        return res

"""
presumably, need to calc the largest area formed between the 2 bars (2 heights)
so to maximize area, we need to max both x and y dims
(aka x (distance between the bars) and y(heights of the 2 bars))
heights int array (list) is in order (use indices)
w x h = area
max each one for max area
to compare different heights[i]'s with each other for max area, need 2 pointers
to iterate thru array
height of the container is the shorter of the 2 bars
need to move pointer with min height inward to find all meaningful combinations (areas)
(keep the higher height and move the other pointer inward)

T: O(N)
S: O(1)

# my first attempt

maximum_area = 0

        for i, h in enumerate(heights):
            l, r = 0, len(heights) - 1  # 2 pointers, indices of heights
            while l < r:
                min_height = min(heights[l], heights[r])
                width = r - l  # distance between compared indices
                area = min_height * width
                if area > maximum_area:
                    maximum_area = area
                l += 1
                r -= 1

        return maximum_area  # int
"""