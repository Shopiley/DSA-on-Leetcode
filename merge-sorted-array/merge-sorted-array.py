class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1Copy = nums1[:m]
        p1 = 0
        p2 = 0

        for i in range(m+n):
            if p2 >= n or (p1 < m and nums1Copy[p1] <= nums2[p2]):
                nums1[i] = nums1Copy[p1]
                p1 += 1

            # p2 < n and (p1 >= m or nums1Copy[p1] > nums2[p2])
            else:
                nums1[i] = nums2[p2]
                p2 += 1


 
        

            
        
        