class Stack:
    '''
        Implement a Stack using built-in python list/array
    '''

    def __init__(self, data=None):
        '''
            Constructs a Stack with given maxsize (defaults to 10)
            Allows creation of an initially empty Stack

            Stack is implemented using list/array
                - push() = list.append()
                - pop()  = list.pop(len(list) - 1)
                - peek() =  the_list[len(list) - 1]

                - top of Stack = last elem in list
                - bottom of Stack = first elem in list
                - top = bottom = None when Stack is empty
        '''
        self._list = []

        if data:
            self._list.append(data)

    def peek(self):
        '''
            Return data at topmost node.  Topmost node stays at top.
        '''
        if bool(self._list):
            return self._list[len(self._list) - 1]

    def push(self, data):
        '''
            Store data at a new topmost node.
        '''
        if data:
            self._list.append(data)

    def pop(self):
        '''
            Return data at topmost node.  Next node below becomes topmost node
        '''
        if bool(self._list):
            return self._list.pop(len(self._list) - 1)

    def is_empty(self):
        '''
            Returns True if Stack contains no node, False otherwise
        '''
        return bool(self._list)

    def __str__(self):
        return str(self._list)


if __name__ == "__main__":
    aStack = Stack()

    print(f'CREATE AND PUSH SOME VALUES ONTO STACK ....')
    aStack.push('hello')
    aStack.push('there')
    aStack.push('ahoy')
    print(aStack)

    print(f'PEEKING ...')
    print(aStack.peek())

    print(f'POPPING ....')
    print(aStack.pop())

    print(f"PUSHING ANOTHER VALUE ....")
    aStack.push(5)
    print(aStack)

    print(f'MORE POPPING ....')
    print(aStack.pop())
    print(aStack.pop())
    print(aStack.pop())
    print(aStack.pop())
