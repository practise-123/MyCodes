# Created by        : MyWork
# Created on        : 2024-07-01
"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array.
Otherwise, return false.
"""


class Solution:

    @classmethod
    def three_consecutive_odds(cls, arr: list[int]) -> bool:
        arr = [str(_ % 2) for _ in arr]
        string = "".join(arr)
        return '111' in string

    @classmethod
    def sol2(cls, arr: list[int]) -> bool:
        found = ""
        i = 0
        while found != "111" and i < len(arr):
            if arr[i] % 2 == 1:
                found += "1"
            else:
                found = ""
            i += 1
        return found == "111"


if __name__ == "__main__":
    pass
