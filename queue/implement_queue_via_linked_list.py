class QueueViaLinkedList:
    '''
        Implement stack via singly-linked list
    '''

    class Node:
        def __init__(self, data=None):
            '''
                Defaults to empty node: data = None, next = None
            '''
            self.data = data
            self.next = None

        def __str__(self):
            return ''.join(['(', str(self.data), ', ', str(self.next), ')'])

    def __init__(self, data=None):
        '''
            Allows an empty queue to be created.
            An empty queue has an empty node.
        '''
        self.first = QueueViaLinkedList.Node()
        self.last = self.first
        self.length = 0

        if data:
            self.enqueue(data)

    def enqueue(self, data):
        '''
            Add entry to end of queue
        '''
        if data:
            new_node = QueueViaLinkedList.Node(data)
            if self.length == 0:
                self.first = new_node
                self.last = new_node
            else:
                self.last.next = new_node
                self.last = new_node

            self.length += 1

    def peek(self):
        '''
            View entry at head of queue
        '''
        if self.length:
            return self.first.data

    def dequeue(self):
        '''
            Get entry at head of queue
        '''
        data = None
        if self.length:
            data = self.first.data
            self.first = self.first.next
            self.length -= 1

        return data

    def is_empty(self):
        return self.length

    def __str__(self):
        this_stack = []
        curr_node = self.first
        while (curr_node):
            # print(f'current node: {curr_node}')
            this_stack.append(curr_node.data)
            curr_node = curr_node.next

        return str(this_stack)


if __name__ == "__main__":
    aQueue = QueueViaLinkedList()
    print(aQueue)

    print(f'CREATE AND ENQUEUE SOME VALUES ONTO QUEUE ....')
    aQueue.enqueue('hello')
    print(aQueue)
    aQueue.enqueue('there')

    aQueue.enqueue('ahoy')
    print(aQueue)

    print(f'PEEKING ...')
    print(aQueue.peek())

    print(f'DEQUEUING ....')
    print(aQueue.dequeue())

    print(f"ENQUEUEING ANOTHER VALUE ....")
    aQueue.enqueue(5)
    print(aQueue)

    print(f'MORE DEQUEUEING ....')
    print(aQueue.dequeue())
    print(aQueue.dequeue())
    print(aQueue.dequeue())

    print(f'DEQUEUING EMPTY QUEUE ....')
    print(aQueue.dequeue())

    print(f"ENQUEUEING MORE VALUES ....")
    vals = [x for x in range(100, 200, 10)]
    for v in vals:
        aQueue.enqueue(v)
    print(aQueue)
