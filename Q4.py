# T is tree represented by matrix
# T[i][j]=1 if i is the parent of j, otherwise 0
# r is root , n1 and n2 are nodes
def question4(T, r, n1, n2):
    if len(T)==0:
        return 'please input the matrix'
    if len(T)==1:
        return 0
    # capture the ancestors of n1
    ancestors1=[]     # list of ancestors of n1
    parent1=None    #record the parent of n1
    while parent1!=r:   # traverse until reach the root (root has no parent)
        for i in range(len(T)):     # search all the ancestors of n1
            if T[i][n1] == 1:  # if i is the parent of n1
                parent1=i
                ancestors1.append(parent1)
                n1 = parent1    # find the parent of n1's parent

    # capture the ancestors of n2
    ancestors2=[]     # list of ancestors of n2
    parent2=None    #record the parent n2
    while parent2!=r:   # traverse until reach the root (root has no parent)
        for i in range(len(T)):     # search all the ancestors of n2
            if T[i][n2] == 1:  # if i is the parent of n2
                parent2=i
                ancestors2.append(parent2)
                n2 = parent2    # find the parent of n2's parent

    # find the first common ancestor of n1 and n2 and turn
    for p1 in ancestors1:
        for p2 in ancestors2:
            if p1==p2:
                return p1

    # otherwise, return the root
    return r


# test
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 4)

print question4([[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0]],
                 3,
                 0,
                 4)
print question4([], 0, 0, 0)
print question4([0], 0, 0, 0)

