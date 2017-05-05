# find the longest palindrome

# helper function to judge whether it is palindromes or not
def isPalindromes(string):
    if string==string[::-1]:
        return True
    return False

# function returen the longest palindromes
def question2(string):
    length=len(string)
    palindromes=''
    temp=''
    for n in range(length):
        for m in range(n):
            substring=string[m:n+1]          # traverse all the combinations
            if isPalindromes(substring):
                temp=substring     # if true, give the value to palindromes
            if len(temp)>len(palindromes):
                palindromes=temp   # update to the longest one
    if len(palindromes)>0:
        return palindromes
    else:
        return 'Sorry, no palindromes found'

# test
print question2('')
print question2('dfertee')
print question2('abccba')
print question2('ethghdxffd')
print question2('bduisfgiuosdgiudggtdbfosdfsdfbislidofhbuisd')
print question2('a')


