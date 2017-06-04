"""
Sherlock and the Valid String
https://www.hackerrank.com/challenges/sherlock-and-valid-string

Sherlock considers a string, , to be valid if either of the following conditions are satisfied:

All characters in  have the same exact frequency (i.e., occur the same number of times). For example,  is valid, but  is not valid.
Deleting exactly  character from  will result in all its characters having the same frequency. For example,  and  are valid because all their letters will have the same frequency if we remove occurrence of c, but  is not valid because we'd need to remove  characters.
Given , can you determine if it's valid or not? If it's valid, print YES on a new line; otherwise, print NO instead.

Input Format

A single string denoting .

Constraints

String  consists of lowercase letters only (i.e., [a-z]).
Output Format

Print YES if string  is valid; otherwise, print NO instead.

Sample Input 0

aabbcd
Sample Output 0

NO
"""

import sys
from collections import Counter

    
def isValid(s):
    # Empty string satisfies the criteria
    if not s:
        return True
    
    # Get the character counts
    # For aabbccc the result will be {'b': 2, 'c': 3, 'a': 2}
    counter = Counter()
    for c in s:
        counter[c] += 1

    # Get counts of counts
    # For aabbccc the result will be {2: 2, 3: 1}
    counts = counter.values()
    counter.clear()
    for count in counts:
        counter[count] += 1
    
    keys = counter.keys()
    values = [counter[key] for key in counter]
    if len(keys) == 1:
        return True
    
    # If there are more then 2 counts, we can't satisfy the criteria
    if len(keys) != 2:
        return False
    
    # One of the counts of counts should be 1
    if not (values[0] == 1 or values[1] == 1):
        return False
    
    # The count that happened 1 times, needs to be either 1 or the other count + 1
    if values[0] == 1:
        if keys[0] == 1 or keys[0] == keys[1] + 1:
            return True

    if values[1] == 1:
        if keys[1] == 1 or keys[1] == keys[0] + 1:
            return True
    
    return False


s = raw_input().strip()
is_valid = isValid(s)
output = 'YES' if is_valid else 'NO'
print(output)
