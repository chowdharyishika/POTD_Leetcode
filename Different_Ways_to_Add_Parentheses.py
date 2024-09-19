'''
PROBLEM: 241. Different Ways to Add Parentheses

APPROACH 1: Recursion
We have strings of operators (+,-,*) and operands (0-9). We can divide the string recursively into left and right parts.
The division will be on the basis of operators.
Conditions: 
if the expression is only a digit: return a list with that number
if the expression contains to number: first is a digit, the second must also be a digit. We convert the expression to a number and return it in a list.
else: divide the expression into left and right part; store all left and right parts in the list; compute each left part with right based
on operator and append it to the result.

APPROACH 2: We can optimise approach 1 by using DP.
'''

# APPROACH 1
def diffWaysToCompute(expression):
        def solve(expression):
            if expression.isdigit():
                return [int(expression)]
            result=[]

            for i in range(len(expression)):
                if expression[i] in ["+","-","*"]:
                    leftpart= solve(expression[:i])
                    rightpart= solve(expression[i+1:])

                    for left in leftpart:
                        for right in rightpart:
                            if expression[i] =="+":
                                result.append(left+right)
                            elif expression[i] =="-":
                                result.append(left-right)
                            elif expression[i] =="*":
                                result.append(left*right)
            return result
        return solve(expression)


expression= "2*3-4*5"
print(diffWaysToCompute(expression))
