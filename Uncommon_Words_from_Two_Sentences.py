'''
PROBLEM: 884. Uncommon Words from Two Sentences

APPROACH 1: Create a dictionary that stores the frequency of words. Find the words that occurs only once and does not occur in other string.
APPROACH 2: Similar to one, except in this we will create only one common frequency dictionary. If the word occurs once, it will be added
in the ans.

'''

# APPROACH 1
from collections import Counter
def uncommonFromSentences(s1, s2):
        ans=set()
        S1=list(s1.split())
        S2=list(s2.split())
        dict_s1=Counter(S1)
        dict_s2=Counter(S2)
        for key, value in dict_s1.items():
            if value==1 and key not in dict_s2:
                ans.add(key)
        for key, value in dict_s2.items():
            if value==1 and key not in dict_s1:
                ans.add(key)
        ans=list(ans)
        return ans

s1= "this apple is sweet"
s2= "this apple is sour"
print(uncommonFromSentences(s1, s2))