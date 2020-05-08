class BinarySearchTree:
    '''
        Implement binary tree in python
    '''

    class Node:
        def __init__(self, data=None):
            self.parent = None
            self.left = None
            self.right = None
            self.data = data

        def __str__(self):
            return ''.join(['\tdata: ', str(self.data), '\n',
                            '\tleft:',  str(self.left), '\n',
                            '\tright:',  str(self.right)])

    def __init__(self, data=None):
        self.root = None

        if data:
            self.insert(data)

    def insert(self, data):
        '''
            Insert data into tree
        '''
        if data:
            node = BinarySearchTree.Node(data)
            if self.root is None:
                # brand new root node
                self.root = node
            else:
                curr_node = self.root
                while curr_node:
                    if data < curr_node.data:
                        # go left if target < curr node's data
                        # when can no longer go left, insert new data there
                        if curr_node.left is None:
                            curr_node.left = node
                            # print(f'insert left:')
                            # print(f'{node}')
                            break
                        curr_node = curr_node.left
                    else:
                        # go right if target > curr node's data
                        # when can no longer go right, insert new data there
                        if curr_node.right is None:
                            curr_node.right = node
                            # print(f'insert right:')
                            # print(f'{node}')
                            break
                        curr_node = curr_node.right

            # self.print_tree()

    def lookup(self, data):
        '''
            Return node that has given data
        '''
        node_found = None
        curr_node = self.root
        while curr_node:
            if data < curr_node.data:
                curr_node = curr_node.left
                if curr_node is None:
                    print(f'not found {data}')
            elif data > curr_node.data:
                curr_node = curr_node.right
                if curr_node is None:
                    print(f'not found {data}')
            else:
                node_found = curr_node
                print(f'found {data}:')
                print(f'{node_found}')
                break
        return node_found

    def get_left_node(self, node):
        return node.left

    def get_right_node(self, node):
        return node.right

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(f'{node.data}')
            self._print_tree(node.right)


if __name__ == "__main__":
    '''
        //     9
        //  4     20
        //1  6  15  170
    '''
    tree = BinarySearchTree()

    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    tree.lookup(4)
    tree.lookup(20)
    tree.lookup(1)
    tree.lookup(100)
