class QueueViaPythonArray:
    '''
        Implement queue using python built-in array/list
    '''

    def __init__(self, data=None):

        # internal array/list to implement queue
        self._mylist = []
        if data:
            self._mylist.append(data)
        self.length = len(self._mylist)

    def enqueue(self, data):
        '''
            Add entry to the end of the array
        '''
        self._mylist.append(data)

    def dequeue(self):
        '''
            Remove entry from head - return entry's data
        '''
        if bool(self._mylist):
            return self._mylist.pop(0)

    def peek(self):
        '''
            View entry at head
        '''
        if bool(self._mylist):
            return self._mylist[0]

    def is_empty(self):
        return len(self._mylist)

    def __str__(self):
        return str(self._mylist)


if __name__ == "__main__":

    aQueue = QueueViaPythonArray()
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
