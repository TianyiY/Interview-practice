def Q1(a, b):
    i = 0   # the first index
    j = -1   # the last index
    # traverse forward and compare each alphabet, until seeing '*'
    while a[i] != '*':
        if a[i] == b[i]:
            i += 1
            if i == len(a):
                break      # if all the alphabets are the same, and no '*' exists, break and return True
        else:
            return False   # if certain alphabets mis-match, return False
    # traverse backward and compare each alphabet, until seeing '*'
    while a[j] != '*':
        if a[j] == b[j]:
            j -= 1
            if -j == len(a) + 1:
                break      # if all the alphabets are the same, and no '*' exists, break and return True
        else:
            return False   # if certain alphabets mis-match, return False
    return True  # return True if all match
# test1
a1='a*b'
b1='acb'
print 'Does "{}" match the pattern of "{}"?  ---{}! '.format(b1, a1, Q1(a1, b1))
# test2
a2='abc*'
b2='abbc'
print 'Does "{}" match the pattern of "{}"?  ---{}! '.format(b2, a2, Q1(a2, b2))
# test3
a3='**bc'
b3='bc'
print 'Does "{}" match the pattern of "{}"?  ---{}! '.format(b3, a3, Q1(a3, b3))
# my test
a='ad*****asftyuydgfds'
b='addyasftyuydgfds'
print 'Does "{}" match the pattern of "{}"?  ---{}! '.format(b, a, Q1(a, b))


''' 
explanation: 
To match the pattern of string a, I traverse from both sides of this string (forward and backward) and compare it with string b, 
if all the characters before and after the '*' macth, then return True, otherwise return False 
if there is no '*' in string a, then compare all the charaters and break the loop, return True 
the time complexity of this algorithm is O(n), n stands for the length of the string 
'''  