
'''
PROBLEM: 1684. Count the Number of Consistent Strings
We need to find how many words in the list of words are allowed, i.e. how many words are created using only the characters present in the allowed.
'''

'''
APPROACH 1: Brute Force
Initialize a counter.
Iterate through word in words array. Check for each word.
Iterate through character of a word and compare if it is allowed or not.
If there is any character that is not allowed break at that time. Else if all the characters are allowed, increment the counter.

APPROACH 2: Boolean Array
As we know all the characters are small letters of English alphabet and we do not need to check the number of each character, 
we can create an boolean array of 26 length, each position representing allowed and not allowed characters.
Then iterate through the list of words, compare it with boolean array and increment the counter accordingly.

APPROACH 3: Hash Set 
Initialize a counter.
Iterate through word in words array. Check for each word. Convert it into set as we need to check only the existence of allowed characters 
and not their frequency. This will optimize the number of iterations through each character of word.
Iterate through character of a word and compare if it is allowed or not.
If there is any character that is not allowed break at that time. Else if all the characters are allowed, increment the counter.

APPROACH 4: Bit Mask
We can use bits of integer (32 bits) as boolean array. There are 32 bits and 26 characters to be checked for allowance. 0th bit will represent a,
1st will represent b and so on.
Two main functions are to be performed.
1. Setting the bit: To show if the specific letter is present or not. We are using bitwise OR for this.
1 (set) will represent present and 0 (not set) will represent absent.
2. Checking the bit: Check if the character is allowed or not. We are using bitwise AND for this. After ANDing each character
1 represent allowed and 0 represent not allowed.

Initialize a counter.
Create bit mask using setting a bit operation.
Check using checking the bit, if there is any bit that is not allowed or inconsistent, break the loop. Else if all are allowed, increment the counter.
'''

# APPROACH 3: Hash Set
def countConsistentStrings_3(allowed, words):
        c=0
        for word in words:
            flag=0
            word=list(set(word))
            for j in word:
                if j not in allowed:
                    flag=1
                    break
            if flag==0:
                c+=1   
        return c

# APPROACH 4: Bit Mask
def countConsistentStrings_4(allowed, words):
        #Create a bitmask
        bit_mask=0

        #Setting the bit
        for ch in allowed:
            bit_mask |=1<<(ord(ch)-ord('a'))

        counter=0

        
        for word in words:
            flag=True

            #Checking for allowed bit
            for i in word:
                bit=(bit_mask >> (ord(i)-ord('a')))&1
            
                if not bit:
                    flag=False
                    break
            if flag:
                counter+=1
        return counter

allowed= "ab"
words= ["ad","bd","aaab","baa","badab"]

print(countConsistentStrings_3(allowed, words))
print(countConsistentStrings_4(allowed, words))