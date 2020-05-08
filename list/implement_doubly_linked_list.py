class DoubleLinkedList:
    '''
        Implements singly linked list using an internal Node class
        DoubleLinkedList requires an initial data value upon construction
    '''

    class Node:
        '''
        '''

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self, data=None):
        node = DoubleLinkedList.Node(data)
        self.head = node
        self.tail = self.head
        self.length = 1

    def append(self, data):
        '''
            Append data at end of list
        '''
        node = DoubleLinkedList.Node(data)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, data):
        '''
            Prepend data at head of list
        '''
        node = DoubleLinkedList.Node(data)
        self.head.prev = node
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
        #   node_before <--> new_node <--> node_after
        if index == 0:
            self.prepend(data)
        elif index == (self.length - 1):
            self.append(data)
        elif (index > 0) and index < (self.length - 1):
            new_node = DoubleLinkedList.Node(data)

            node_before = self.traverse_to_index_before(index)
            node_after = node_before.next

            node_before.next = new_node

            node_after.prev = new_node

            new_node.next = node_after
            new_node.prev = node_before

            self.length += 1
        else:
            # given index is out of valid range
            print(f'given index ({index}) os invalid')

    def remove(self, index):
        '''
            Remove data residing at given index in the list
        '''
        if index == 0:
            # remove the head --> do following in order
            self.head = self.head.next
            self.head.prev = None
        elif index == (self.length - 1):
            node_before = self.traverse_to_index_before(index)
            node_to_remove = node_before.next
            self.tail = node_before
            self.tail.next = None
            node_before.next = node_to_remove.next
        elif (index > 0) and index < (self.length - 1):
            # node_before <--> node_to_remove <--> node_after
            node_before = self.traverse_to_index_before(index)
            node_to_remove = node_before.next
            node_after = node_to_remove.next

            node_before.next = node_to_remove.next
            node_after.prev = node_to_remove.prev

        self.length -= 1

    def reverse(self):
        '''
            Returns a new list with elements in reversed order
        '''
        the_reversed_list = []

        curr_node = self.tail
        while curr_node:
            the_reversed_list.append(curr_node.data)
            curr_node = curr_node.prev
        return the_reversed_list

    def reverse_in_place(self):
        '''
            Original list is modified so that elements are reversed

            Let '+++>' means next pointer
                '--->' means prev pointer
            From:
                A         B +++>   C
                A     <---B        C
            To:
                C         B +++>   A
                C     <---B        A
            Then:
                we want:
                    - B's new next same as B's old prev
                    - B's new prev same as B's old next
        '''

        # current head/tail
        first_node = self.head
        last_node = self.tail

        # new head/tail when reversal is completed
        self.head = last_node
        self.tail = first_node

        node_to_process = first_node
        while node_to_process:
            old_prev = node_to_process.prev
            old_next = node_to_process.next

            node_to_process.next = old_prev
            node_to_process.prev = old_next

            node_to_process = old_next

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
    mll = DoubleLinkedList(10)
    print(mll)

    # mll.append(5)
    # print(mll)

    # mll.append(16)
    # print(mll)

    # mll.prepend(1)
    # print(mll)

    # mll.insert(0, 2)
    # print(mll)

    # mll.insert(4, 200)
    # print(mll)

    # mll.insert(3, 1200)
    # print(mll)

    # mll.insert(len(mll) - 1, 5000)
    # print(mll)

    # mll.insert(len(mll), 6000)
    # print(mll)

    # mll.remove(0)
    # print(mll)

    # mll.remove(len(mll) - 1)
    # print(mll)

    # mll.remove(2)
    # print(mll)

    # using the prev pointer from now on
    print(f'EXERCISING PREV POINTER .... NEW LIST IN REVERSE DIRECTION')
    mll.append(5)
    print(mll.reverse())

    mll.append(16)
    print(mll.reverse())

    mll.prepend(2)
    print(mll.reverse())

    mll.prepend(1)
    print(mll.reverse())

    mll.insert(2, 100)
    print(mll.reverse())

    mll.insert(4, 200)
    print(mll.reverse())

    mll.remove(3)
    print(mll.reverse())

    print(f'THE LIST IN FORWARD DIRECTION ....')
    print(mll)

    print(f'REVERSE THE LIST IN PLACE ....')
    # note that reverse_in_plae() returns nothing (i.e. None)
    mll.reverse_in_place()
    print(mll)
    print(f'list length = {len(mll)}')
