class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        res = 1
        cur = 1
        i = 0
        l = len(arr)

        # Case 1
        while i < l:

            if i % 2 == 0:
                if i + 1 < l and arr[i] < arr[i+1]:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 1
            else:
                if i + 1 < l and arr[i] > arr[i+1]:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 1

            i += 1

        # Case 2
        i   = 0
        cur = 1
        while i < l:

            if i % 2 != 0:
                if i + 1 < l and arr[i] < arr[i+1]:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 1
            else:
                if i + 1 < l and arr[i] > arr[i+1]:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 1

            i += 1




        
        return res

