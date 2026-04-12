class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        old_value = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            new_value = max(old_value, arr[i+1])
            old_value = arr[i]
            arr[i] = new_value

        return arr