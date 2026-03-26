class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Set pointers for nums1, nums2, and the end of nums1
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        # While there are elements to compare in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If any elements remain in nums2, copy them
        # (Remaining elements in nums1 are already in place)
        nums1[:p2 + 1] = nums2[:p2 + 1]