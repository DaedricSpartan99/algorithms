class LinkedListIterator:
    def __init__(self, key, previous, next_):
        # stored key
        self.key = key
        # previous pointer in the list
        self.prevptr = previous
        # next pointer in the list
        self.nextptr = next_


class LinkedList:
    def __init__(self):
        self.head = None

    # linear search inside the linked list
    # returns the LinkedListIterator associated with key
    def search(self, key):
        # initialize iterator as the head
        x = self.head

        # advance while:
        #   - the iterator is not the list terminator
        #   - the current key is different from key
        while x is not None  and x.key != key:
            x = x.nextptr

        return x
    
    # insert an element before the head of the list
    # x is a LinkedListIterator
    def insert(self, x):
        # link head as next element of x
        x.nextptr = self.head

        # if not empty, link x as previous element of head
        if self.head is not None:
            self.head.prevptr = x
        
        # reassign the head
        self.head = x

        # no element before x
        x.prev = None

    def delete(self, x):
        # if not first element:
        # link next element as (next of the previous one)
        # otherwise set second element as head
        if x.prevptr is not None:
            x.prevptr.nextptr = x.nextptr
        else:
            self.head = x.nextptr

        # if not last element:
        # set previous element as (previous of the next one)
        if x.nextptr is not None:
            x.nextptr.prevptr = x.prevptr


