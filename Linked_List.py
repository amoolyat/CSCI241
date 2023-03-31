class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = self.__Node(0)
        self.__trailer = self.__Node(0)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0
        self.__curr = None
        self.__iter_index = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size


    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        node = Linked_List.__Node(val)
        node.prev = self.__trailer.prev
        node.prev.next = node
        node.next = self.__trailer
        self.__trailer.prev = node
        self.__size += 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        if self.__size == 0 or index >= self.__size or index < 0:
            raise IndexError
        node = Linked_List.__Node(val)
        if index == 0:
            node.next = self.__header.next
            self.__header.next = node
            node.prev = self.__header
            node.next.prev = node 
        else:
            curr = self.__header
            count = 0
            while curr is not None and curr.next is not None and count < index:
                curr = curr.next
                count += 1
            
            nextNode = curr.next
            node.prev = curr
            node.next = nextNode
            nextNode.prev = node
            curr.next = node
        self.__size += 1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if self.__size == 0 or index >= self.__size or index < 0:
            raise IndexError
        if index == 0:
            temp = self.__header.next.val
            self.__header.next = self.__header.next.next
            self.__header.next.prev = self.__header
            self.__size -= 1
            return temp
    
        else:
            curr = self.__header
            count = 0
            
            while curr is not None and curr.next is not None and count < index:
                curr = curr.next
                count += 1
            
            node = curr.next
            afterNode = node.next
            curr.next = afterNode
            afterNode.prev = curr
            node.prev = None
            node.next = None
            self.__size -= 1
            return node.val

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if self.__size == 0 or index >= self.__size or index < 0:
            raise IndexError
        count = 0 
        curr = self.__header
        while curr.next is not None and count <= index:
            curr = curr.next
            count += 1
        return curr.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__size != 0:
            curr = self.__header.next
            self.__header.next = curr.next
            curr.next.prev = self.__header

            curr.prev = self.__trailer.prev
            curr.next = self.__trailer   
            self.__trailer.prev.next = curr
            self.__trailer.prev = curr
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        val = ""
        curr = self.__header.next
        while curr and curr != self.__trailer:
            val += str(curr.val) + ", "
            curr = curr.next
        val = val.strip(", ")
        if len(val):
            return "[ " + val + " ]"
        else:
            return "[ ]"

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__curr = self.__header.next
        self.__iter_index = 0
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__curr == self.__trailer:
            raise StopIteration
        to_return = self.__curr.val
        self.__curr = self.__curr.next
        self.__iter_index += 1
        return to_return

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        ll = Linked_List()
        ll_curr = ll.__header
        curr = self.__trailer.prev
        
        while curr is not None and curr != self.__header:
            n = Linked_List.__Node(curr.val)
            ll.__size +=1
            ll_curr.next = n
            ll_curr.next.prev = ll_curr
            ll.__trailer.prev = n
            ll.__trailer.prev.next = ll.__trailer
            curr = curr.prev
            ll_curr = ll_curr.next
        return ll

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests    
   
    ll = Linked_List()
    
    #checking to see if it returns None when rotating an empty LL
    print(ll.rotate_left())
    
    #testing append_element
    
    ll.append_element(-1)
    ll.append_element('literally')
    ll.append_element('love')
    ll.append_element('linked')
    ll.append_element('lists')
    
    print('Length of LL: ' + str(len(ll)))
    
    #testing insert_element_at
    
    ll.insert_element_at(4,0)
    ll.insert_element_at(3,0)
    ll.insert_element_at(8,0)
    ll.insert_element_at(2,1)
    ll.insert_element_at(9,2)
    print(ll)
    
    try:
        ll.insert_element_at(50, -200)
        ll.insert_element_at(2, 56)
    except IndexError:
        print('Caught index error for insert element')
    
    #testing get_element_at
    
    print(ll.get_element_at(0))
    print(ll.get_element_at(1))
    
    try:
        ll.get_element_at(-1)
        ll.get_element_at(100)
        ll.get_element_at(10)
    except IndexError:
        print('Caught index error for get element')
    
    #should not add anything or increase size
    ll.append_element(None)
    print('Length of LL: ' + str(len(ll)))
    
    ll.remove_element_at(2)
    ll.remove_element_at(0)
    print(ll)
    
    try:
        ll.remove_element_at(50)
        ll.remove_element_at(-5)
    except IndexError:
        print('Caught index error for remove element')
    
    #testing rotate left method
    ll.rotate_left()
    print(ll)
    ll.rotate_left()
    print(ll)

    #iter index + next check
    lonklist = Linked_List()
    lonklist.append_element(1)
    lonklist.append_element(2)
    lonklist.append_element(0)
    lonklist.append_element(8)
    lonklist.append_element(2)
    print(lonklist)
    for val in lonklist:
        print(str(val))
    
