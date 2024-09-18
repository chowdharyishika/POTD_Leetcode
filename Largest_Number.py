'''
PROBLEM: 179. Largest Number

APPROACH 1: Create a custom comaparator to sort the numbers.
To get the desired result, we can compare two numbers a and b as: if a+b > b+a ; put a before b else put b before a (here + denotes concatenation of two numbers)

In python we can use cmp_to_key() to implement this as lambda uses key which cannot implement this.
Other method is to replicate the number multiple times and then compare. For example if we have to compare 3 and 30,
replicate both 10 times( according to the constraint ) the numbers become 3333333333 and 30303030303030303030. When we compare both 3 will
come before 30 which is the desired result ( because 303 < 330)

APPROACH 2: Use divide and conquer techniques like merge sort and quick sort and apply the same comparator mentioned in Approach 1.
'''

# APPROACH 1
def largestNumber(nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num_str=[str(i) for i in nums]

        num_str.sort(key= lambda a: a*10, reverse =True)

        if num_str[0] =='0':
            return "0"
        
        return "".join(num_str)

nums= [3,30,34,5,9]
print(largestNumber(nums))
