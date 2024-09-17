'''
PROBLEM: 1310. XOR Queries of a Subarray
APPROACH 1: Brute Force
In queries the left and right pointers are given. We can use nested loops. The outer loop will iterate through queries array.
The inner loop will run from left to right boundary and each boundary will each time XOR the elements from left boundary to right boundary.

APPROACH 2: Prefix Array used
In this we can store xor of elements in a prefix xor array. We know that XOR of elements twice gives the resultant 0 i.e, A^A=0
So to find the XOR from left boundary to right we can use result[i]=prefix_xor[left-1]^prefix_xor[right]
for each queries[i]
This will eliminate the use of nested loop.

APPROACH 3: In place prefix array
Instead of using space to store prefix array we can use the arr array to store the prefix xor.
'''

#APPROACH 2
def xorQueries(arr, queries):
        prefix_xor= [0]*(len(arr)+1)
        prefix_xor[0]=arr[0]
        for i in range(1,len(arr)):
            prefix_xor[i]=prefix_xor[i-1]^arr[i]
        
        result=[]
        for left,right in queries:
            result.append(prefix_xor[left-1]^prefix_xor[right])
        return result

arr= [1,3,4,8]
queries= [[0,1],[1,2],[0,3],[3,3]]
print(xorQueries(arr, queries))