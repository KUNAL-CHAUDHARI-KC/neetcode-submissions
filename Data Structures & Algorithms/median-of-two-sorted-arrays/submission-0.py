class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        l, r = 0, m
        half = (m + n + 1) // 2

        while l <= r:
            partition1 = (l + r) // 2
            partition2 = half - partition1

            # Values immediately around both partitions
            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right1 = float('inf') if partition1 == m else nums1[partition1]

            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]

            # Correct partition found
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2:
                    return float(max(left1, left2))

                return (max(left1, left2) + min(right1, right2)) / 2

            # nums1 partition is too far right
            elif left1 > right2:
                r = partition1 - 1

            # nums1 partition is too far left
            else:
                l = partition1 + 1

        return 0.0