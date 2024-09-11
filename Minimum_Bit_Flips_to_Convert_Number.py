'''
PROBLEM: 2220. Minimum Bit Flips to Convert Number
APPROACH: We need to find the different bits at a position. First XOR is used to find the different bits.
For each different bit XOR operation will set(1) the particular position
An "int" type has 32 bits so range goes from 0 to 31 to iterate through the bits of a number. 
We need to check the set bits and for each set bit increment the counter by 1.
'''

def minBitFlips(start, goal):
        ans=start^goal
        c=0
        for i in range(31):
            if ans&(1<<i):
                c+=1
        return c


start=7
goal=10
print(minBitFlips(start, goal))