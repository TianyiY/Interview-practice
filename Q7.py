import copy
# strings used to test
string='1123'
#string='11234567234'
# dictionary
dictionary={'1':'a', '2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o',
            '16': 'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z'}
# make a 2D-array to store the combinations, initialize by single digits
list = [[string[i] for i in range(len(string))]]
list0 = list[0]   # 1D-array of the first combination
# define function Q2 to concatenate the consecutive digits
def Q2(arr, l=0, r=len(string)-1):
    for i in range(l, r):
        new = copy.deepcopy(arr)
        new[i] = new[i] + new[i + 1]
        del new[i + 1]
        list.append(new)
        Q2(new, l=i+1, r=len(new)-1) # recursively call Q2 to make all the possible combinations
    return list # return the combination list
# define function conversion to convert digits combination to string combination
def conversion(list):
    char = []
    # this loop converts numbers into string, if the numbers are not in dictionary, make them 'NAN'
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] in dictionary:
                str = dictionary.get(list[i][j])
                char.append(str)
            else:
                str = 'NAN'
                char.append(str)
    char_ = char[::-1] # reverse the order, for pop()
    char2 = []
    temp = []
    # this loop drops all the combinations include 'NAN'
    for i in range(len(list)):
        for j in range(len(list[i])):
            str2 = char_.pop()
            temp.append(str2)
        char2.append(temp)
        temp = []
    fin_char = []
    for i in range(len(char2)):
        if 'NAN' not in char2[i]:
            fin_char.append(char2[i])
    return fin_char
# test
list=Q2(arr=list0)
fin_char=conversion(list)
print 'The potential string combinations of {} are: {}. There are {} different kinds of combinations'.format(string, fin_char, len(fin_char))


''' 
explanation: 
firstly, I make a dictionary and a 2D list to store the potential string combinations 
Secondly, I create the first string combination list0, all are single digit 
Because there are only 26 alphabets, I only need to concatenate the consecutive two digits 
Thirdly, I define function Q2 to concatenate consecutive digits 
Then resursively call this function to make all the possible concatenation 
Lastly, convert the digits to string combination by function conversion, drop all the combinations which include invalid elements(number>26) 
The time complexity can reach O(n^2), where n is the length of string 
'''