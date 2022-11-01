#Given an array arr, replace every element in that array with the greatest element among the elements to its right,
#  and replace the last element with -1.

# solution 1, best case
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # iniitialize max
        max_arr = -1
        # get the length of the arrary

        k = len(arr)-1

        # reverse
        while k >= 0:
            tmp = arr[k]
            arr[k] = max_arr # set the last item to -1
            if tmp > max_arr:
                max_arr = tmp   # swap max; update the max value
            k -= 1
        return arr

# solution 2 with for loops
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last_ele = -1

        for i in range(len(arr)-1, -1, -1):
            tmp = arr[i]
            arr[i] = last_ele
            if tmp > last_ele:
                last_ele = tmp
        return arr