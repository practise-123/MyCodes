# Created by        : MyWork
# Created on        : 2024-07-02
"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays ,
and you may return the result in any order.
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums2) < len(nums1):
            lst1, lst2 = nums2, nums1
        else:
            lst1, lst2 = nums1, nums2
        result = []
        for i in lst1:
            if i in lst2:
                lst2.pop(lst2.index(i))
                result.append(i)
        return result
