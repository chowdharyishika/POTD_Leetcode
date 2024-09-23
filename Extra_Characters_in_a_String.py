'''
PROBLEM: 2707. Extra Characters in a String

APPROACH: Top to bottom DP
We'll maintain cache which will basically hold the key as length of the selected text from s
and value as the minimum extra letters in the given length of text.
CASES:
1. if text="" : there is no text hence return 0
2. if given length of text is already present in cache - there is no need to solve [usage of DP]
3. now we will iterate in dictionary
if text matches with any of the word present in dictionary, then it means there is no extra letter in it therefore update the cache;
return minimum as 0
if it partially matches then call the function for text after the length of the word
Update the minimum, cache and return minimum.
'''

def minExtraChar(s, dictionary):
        cache={}

        def dfs(text):
            if len(text)<=0:
                return 0
            
            if len(text) in cache:
                return cache[len(text)]
            
            minimum =len(text)

            for word in dictionary:
                if text==word:
                    minimum=0
                    cache[len(text)]= minimum

                    return minimum
                
                elif text[:len(word)] == word:
                    result=dfs(text[len(word):])
                    minimum =min(minimum, result)
            
            minimum= min(minimum, 1+dfs(text[1:]))
            cache[len(text)]=minimum
            return minimum
        return dfs(s)

s="leetscode"
dictionary= ["leet","code","leetcode"]
print(minExtraChar(s, dictionary))