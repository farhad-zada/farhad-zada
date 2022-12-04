# SPDX-License-Identifier: MIT
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        
        left = nums[0]; l = 1; right = sum(nums[1:]); r = len(nums) - 1;
        
        min_avg = abs((left//l) - (right//r)); index = 0; 
        
        for i, n in enumerate(nums[1:], 1):
            
            right -= n; left += n; r -= 1; l += 1;
            
            a = (left//l)
            try: 
                b = (right//r)
            except:
                b = 0
            cur = abs(a - b)
            
            if cur < min_avg: 
                index = i; 
                min_avg = cur 
        return index
        