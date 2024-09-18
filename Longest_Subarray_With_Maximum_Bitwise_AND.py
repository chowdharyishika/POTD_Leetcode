'''
PROBLEM: 2419. Longest Subarray With Maximum Bitwise AND

APPROACH: We know that ANDing the maximum numbers will give the maximum value. So we need to find the subarray with maximum value numbers.
Remember these 3 tips in Bit manipulation -
X ^ X = 0,
X & X <= X,
X | X >= X

Iterate through the nums array.
Maintain result which stores the maximum length of subarray; max_val which stores the maximum value after ANDing the numbers;
curr which stores the current maximum length of subarray

if nums[i] > max_value: update the max_value and set curr and ans as 0 because it becomes the inflection point
if nums[i] == max_value: increment curr by 1 
else update curr=0  as again it becomes an inflection point

at the end of each iteration update result.
'''

#APPROACH 
def longestSubarray(nums):
        max_val=curr=ans=0
        for i in nums:
            if max_val<i:
                max_val=i
                ans=curr=0
            
            if max_val==i:
                curr+=1
            else:
                curr=0
            ans=max(ans, curr)
        return ans
nums= [1,2,3,3,2,2]
print(longestSubarray(nums))