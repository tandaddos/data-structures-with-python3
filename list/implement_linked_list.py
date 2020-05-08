class MyLinkedList:
    '''
        Implements singly linked list using an internal Node class
        MyLinkedList requires an initial data value upon construction
    '''

    class Node:
        '''
        '''

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, data=None):
        node = MyLinkedList.Node(data)
        self.head = node
        self.tail = self.head
        self.length = 1

    def append(self, data):
        '''
            Append data at end of list
        '''
        node = MyLinkedList.Node(data)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, data):
        '''
            Prepend data at head of list
        '''
        node = MyLinkedList.Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def traverse_to_index_before(self, index):
        # traverse to the node before the node referenced by given index
        node = self.head
        for i in range(index - 1):
            node = node.next
        return node

    def insert(self, index, data):
        '''
            Iinsert data so that the resulting node is at given index in list.
            List indexing starts at 0
        '''
        # the new data will be positioned at current location of given index
        # readjust pointers accordingly
        if index == 0:
            self.prepend(data)
        elif index == (self.length - 1):
            self.append(data)
        elif (index > 0) and index < (self.length - 1):
            new_node = MyLinkedList.Node(data)
            node = self.head
            for i in range(index - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
            self.length += 1
        else:
            # given index is out of valid range
            print(f'given index ({index}) os invalid')

    def remove(self, index):
        '''
            Remove data residing at given index in the list
        '''
        if index == 0:
            self.head = self.head.next
        elif index == (self.length - 1):
            node_before = self.traverse_to_index_before(index)
            node_to_remove = node_before.next
            self.tail = node_before
            self.tail.next = None
            node_before.next = node_to_remove.next
        elif (index > 0) and index < (self.length - 1):
            node_before = self.traverse_to_index_before(index)
            node_to_remove = node_before.next
            node_before.next = node_to_remove.next

        self.length -= 1

    def reverse_in_place(self):
        '''
            Reverse list in place by making use of the fact that for any node:
                - we can get to its next node
                - we can 'save' its previous node
                - change its next pointer to point to previous node
        '''
        # starting out with current node being the head
        # and previous node being None
        curr_node = self.head
        prev_node = None

        # after reversal is completed
        self.head = self.tail
        self.tail = curr_node

        while curr_node:
            # mark where next node is ...
            next_node = curr_node.next

            # change this node's next to point to previous node
            curr_node.next = prev_node

            # move on to next node
            prev_node = curr_node
            curr_node = next_node

    def __str__(self):
        the_list = []

        node = self.head
        while node:
            the_list.append(node.data)
            node = node.next
        return str(the_list)

    def __len__(self):
        return self.length


if __name__ == "__main__":
    mll = MyLinkedList(10)
    print(mll)

    mll.append(5)
    print(mll)

    mll.append(16)
    print(mll)

    mll.prepend(1)
    print(mll)

    mll.insert(0, 2)
    print(mll)

    mll.insert(4, 200)
    print(mll)

    mll.insert(3, 1200)
    print(mll)

    mll.insert(len(mll) - 1, 5000)
    print(mll)

    mll.insert(len(mll), 6000)
    print(mll)

    mll.remove(0)
    print(mll)

    mll.remove(len(mll) - 1)
    print(mll)

    mll.remove(2)
    print(mll)

    print(f'REVERSE LIST IN PLACE ....')
    # note that reverse_in_plae() returns nothing (i.e. None)
    mll.reverse_in_place()
    print(mll)
    print(f'list length = {len(mll)}')
