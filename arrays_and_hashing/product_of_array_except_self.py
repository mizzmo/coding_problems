# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer. 

# Attempt 1 : Division
# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution0:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Keep track of the total product and the number of zeros that appear.
        total_product = 0
        zero_count = 0 
        output = [0] * len(nums)
        # For every element
        for i in range(len(nums)):
            # If zero appears, add to count.
            if nums[i] == 0:
                zero_count += 1
            else:
                # Otherwise add to running product.
                if total_product == 0:
                    total_product = nums[i]
                else:  
                    total_product = int(total_product * nums[i])

        if zero_count == 0:
            for j in range(len(nums)):
                # Divide by the value at nums[i] to get product at that slot.
                output[j] = int(total_product / nums[j])
        elif zero_count > 1:
            return [0] * len(nums) 
        else:
            # Find where the zeroes are and set to the total product.
            for j in range(len(nums)):
                if nums[j] == 0:
                    output[j] = total_product
                else:
                    output[j] = 0
            
        return output
    
# Attempt 2 - Prefix and Postfix
# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix Array
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                prefix[i] = prefix[i-1] * nums[i]
            else:
                prefix[i] = nums[i]

        # Postfix Array
        postfix = [0] * len(nums)
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                postfix[j] = nums[j]
            else:
                postfix[j] = postfix[j+1] * nums[j]

        # Multiply prefix[i-1] by postfix[i+1]
        output = [0] * len(nums)
        for k in range(len(nums)):
            # Handle edge cases
            if k == 0:
                output[k] = 1 * postfix[k+1]
            elif k == len(nums)-1:
                output[k] = prefix[k-1] * 1
            else:
                output[k] = prefix[k-1] * postfix[k+1]

        return output


# Model Solution - Prefix & Suffix
# Time Complexity - O(n)
# Space Complexity - O(1)
class SolutionM:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res