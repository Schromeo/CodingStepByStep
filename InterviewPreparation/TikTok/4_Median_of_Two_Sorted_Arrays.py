class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            px = (low + high ) // 2
            py = (x + y + 1) // 2 - px

            leftx  = float('-inf') if px == 0 else nums1[px - 1]
            rightx = float('inf')  if px == x else nums1[px]
            lefty  = float('-inf') if py == 0 else nums2[py - 1]
            righty = float('inf')  if py == y else nums2[py]

            if leftx <= righty and lefty <= rightx:
                if (x + y) % 2 == 0:
                    return (max(leftx, lefty) + min(rightx, righty)) / 2.0
                else:
                    return float(max(leftx, lefty))
            elif leftx > righty:
                high = px - 1
            else:
                low = px + 1
