class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k will count the elements not equal to val
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                # Move the valid element to the front
                nums[k] = nums[i]
                k += 1
                
        # k is the count of elements that remain
        return k