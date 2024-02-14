class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Separate negative (n) and positive (p) numbers into two lists
        n = []
        p = []
        for i in nums:
            if i < 0:
                n.append(i)
            else:
                p.append(i)
        
        # Initialize pointers for iterating through n, p, and nums
        i = j = k = 0

        # Interleave positive and negative numbers in the original nums list
        while i < len(n) and j < len(p):
            # If the current index is even, place a positive number from p
            if k % 2 == 0:
                nums[k] = p[j]
                j += 1
            # If the current index is odd, place a negative number from n
            else:
                nums[k] = n[i]
                i += 1
            k += 1

        # If there are remaining negative numbers, append them to nums
        while i < len(n):
            nums[k] = n[i]
            i += 1
            k += 1

        # If there are remaining positive numbers, append them to nums
        while j < len(p):
            nums[k] = p[j]
            j += 1
            k += 1

        # Return the modified nums list with interleaved positive and negative numbers
        return nums
