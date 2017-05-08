# class of linked list node
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):   # ll is the first node, m is the "mth number from the end"

    if ll:    # if the linkedlist has been initialized
        length=1   # length of the linkedlist
        temp=ll    # record the node temporarily
        # traverse the linkedlist to calculate the length of linkedlist, since we cannot know its length without traversal
        while temp.next:
            length+=1
            temp=temp.next
        if m>length:
            return 'm is longer than the linkedlist, try again'
        else:
            pos=0
            temp2=ll
            # traverse again to get the position
            while pos<length-m:
                pos+=1
                temp2=temp2.next
            return temp2.data     # return the value of the found node
        return ll.data    # return the value of the first node if there is no following node exist

    # if the first node is not existed
    else:
        return 'linkedlist has not been initialized'




# test
print question5(None, 2)

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
print question5(node1, 1)
print question5(node1, 2)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
print question5(node1, 3)
print question5(node1, 6)
print question5(node4, 3)



