class StackViaLinkedList:
    '''
        Implement stack via singly-linked list
    '''

    class Node:
        def __init__(self, data=None):
            '''
                Defaults to empty StackViaLinkedList.Node: data = None, next = None
            '''
            self.data = data
            self.next = None

    def __init__(self, data=None):
        '''
            Allows an empty stack to be created
        '''
        self.top = StackViaLinkedList.Node()
        self.bottom = self.top
        self.length = 0

        if data:
            self.push(data)

    def push(self, data):
        if data:
            new_node = StackViaLinkedList.Node(data)
            new_node.next = self.top

            self.top = new_node

            if self.length == 0:
                self.bottom = self.top
            self.length += 1

    def peek(self):
        if self.length:
            return self.top.data

    def pop(self):
        data = None
        if self.length:
            data = self.top.data
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                print(
                    f'empty stack: bottom = {self.bottom.next} {self.bottom.data}')

        return data

    def is_empty(self):
        return self.length

    def __str__(self):
        this_stack = []
        curr_node = self.top
        while (curr_node):
            this_stack.append(curr_node.data)
            curr_node = curr_node.next
        return str(this_stack)


if __name__ == "__main__":
    aStack = StackViaLinkedList()

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
