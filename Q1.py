# judge substrings of certain string
# Knuth-Morris-Pratt algorithm is going to be implemented.
def question1(string, substring):

    # make inputs lists
    substring=list(substring)
    string=list(string)

    # build a prefix list
    prefix=[0]*len(substring)
    for m in range(1, len(substring)):
        i=prefix[m-1]
        while i>0 and substring[m]!=substring[i]:
            i=prefix[i-1]
        if substring[m]==substring[i]:
            i+=1
        prefix[m]=i

    # KMP matching
    j=0
    for n in range(0, len(string)):
        while j>0 and string[n]!=substring[j]:
            j=prefix[j-1]
        if string[n]==substring[j]:
            j+=1
            if j==len(substring):
                return True
    return False


# test
print question1('rgfdfgdff', 'rgfdfg')
print question1('rgfdfgdff', 'fdf')
print question1('rgfdfgdff', 'fdfgr')
print question1('rgfdfgdff', 'hff')
print question1('rgfdfgdff', 'rgc')



