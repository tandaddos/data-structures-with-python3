from enum import Enum


class BinarySearchTree:
    '''
        Implement binary tree in python
    '''

    class TreeTraverseOrder(Enum):
        preorder = 'pre-order'
        inorder = 'in-order'
        postorder = 'post-order'

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

    def __init__(self, data=None, debug=False):
        self.root = None
        self.debug = debug

        if data:
            self.insert(data)

    def _debug(self, msg):
        if self.debug:
            print(f'{msg}')

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
                self._debug(f'{node_found}')
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

    def bfs_iterative(self):
        '''
            BFS traversal

            returns list of nodes to be traversed via bfs
        '''
        curr_node = self.root

        # ordered list of nodes traversed by bfs (start from fron)
        nodes_visited = []

        # working list of nodes to be traversed (start from front)
        nodes_to_be_visited = []

        # start the journey ..
        nodes_to_be_visited.append(curr_node)
        while len(nodes_to_be_visited) > 0:
            node = nodes_to_be_visited.pop(0)
            nodes_visited.append(node.data)
            if node.left:
                nodes_to_be_visited.append(node.left)
            if node.right:
                nodes_to_be_visited.append(node.right)
        return nodes_visited

    def _bfs_recurse(self, nodes_visited, nodes_to_be_visited):
        '''
            Helper internal method to bfs recurse
        '''
        if len(nodes_to_be_visited) == 0:
            return nodes_to_be_visited

        node = nodes_to_be_visited.pop(0)
        nodes_visited.append(node.data)

        # gather all of this node's children
        if node.left:
            nodes_to_be_visited.append(node.left)
        if node.right:
            nodes_to_be_visited.append(node.right)

        # go to next lower level
        return self._bfs_recurse(nodes_visited, nodes_to_be_visited)

    def bfs_recursive(self):
        '''
            Public method to do bfs recursively
        '''
        nodes_visited = []
        nodes_to_be_visited = []

        # start the journey ...
        nodes_to_be_visited.append(self.root)
        self._bfs_recurse(nodes_visited, nodes_to_be_visited)
        return nodes_visited

    def _dfs_pre_order_recurse(self, node, nodes_visited):
        '''
            Helper internal method to do dfs recurse

            Traverse order = pre-order
                parent -- left -- right
        '''
        if node is None:
            return node

        nodes_visited.append(node.data)
        self._debug(f'preorder: {nodes_visited}')

        # go down left side as deep as possible
        if node.left:
            self._debug(f'preorder: going left to {node.left.data}')
            self._dfs_pre_order_recurse(node.left, nodes_visited)

        # go down right side as deep as possible
        if node.right:
            self._debug(f'preorder: going right to {node.right.data}')
            self._dfs_pre_order_recurse(node.right, nodes_visited)

    def _dfs_post_order_recurse(self, node, nodes_visited):
        '''
            Helper internal method to do dfs recurse

            Traverse order = post-order
                left -- right -- parent
        '''
        if node is None:
            return node

        # go down left side as deep as possible
        if node.left:
            self._debug(f'postorder: going left to {node.left.data}')
            self._dfs_post_order_recurse(node.left, nodes_visited)

        # go down right side as deep as possible
        if node.right:
            self._debug(f'postorder: going right to {node.right.data}')
            self._dfs_post_order_recurse(node.right, nodes_visited)

        nodes_visited.append(node.data)
        self._debug(f'postorder: {nodes_visited}')

        return nodes_visited

    def _dfs_in_order_recurse(self, node, nodes_visited):
        '''
            Helper internal method to do dfs recurse

            Traverse order = in-order
                left -- parent -- right
        '''
        if node is None:
            return node

        # go down left side as deep as possible
        if node.left:
            self._debug(f'inorder: going left to {node.left.data}')
            self._dfs_in_order_recurse(node.left, nodes_visited)

        nodes_visited.append(node.data)
        self._debug(f'inorder: {nodes_visited}')

        # go down right side as deep as possible
        if node.right:
            self._debug(f'inorder: going right to {node.right.data}')
            self._dfs_in_order_recurse(node.right, nodes_visited)

    def dfs_recursive(self, traversal_order=TreeTraverseOrder.preorder):
        '''
            Public method to do dfs recursively
        '''
        nodes_visited = []

        if traversal_order == BinarySearchTree.TreeTraverseOrder.preorder:
            self._dfs_pre_order_recurse(self.root, nodes_visited)
            return nodes_visited
        elif traversal_order == BinarySearchTree.TreeTraverseOrder.postorder:
            self._dfs_post_order_recurse(self.root, nodes_visited)
            return nodes_visited
        elif traversal_order == BinarySearchTree.TreeTraverseOrder.inorder:
            self._dfs_in_order_recurse(self.root, nodes_visited)
            return nodes_visited


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

    print(f'bfs_iterative: {tree.bfs_iterative()}')
    print(f'bfs_recursive: {tree.bfs_recursive()}')
    print(f'dfs_recursive (preorder): {tree.dfs_recursive()}')
    print(
        f'dfs_recursive (postorder): {tree.dfs_recursive(BinarySearchTree.TreeTraverseOrder.postorder)}')
    print(
        f'dfs_recursive (inorder): {tree.dfs_recursive(BinarySearchTree.TreeTraverseOrder.inorder)}')
