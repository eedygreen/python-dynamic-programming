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