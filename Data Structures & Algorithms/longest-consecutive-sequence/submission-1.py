class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        max_length = 0

        for n in nums:
            if n - 1 not in nums:
                current_num = n
                counter = 1
                while current_num + 1 in nums:
                    current_num += 1
                    counter += 1
                max_length = max(max_length, counter)

        return max_length