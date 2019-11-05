import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, val):
        node = Node(val)
        self.count += 1
        if self.head is None:
            self.head = node
            return

        curr = self.head
        while curr:
            if val < curr.val:
                if curr.left is None:
                    curr.left = node
                    return
                else:
                    curr = curr.left
            else:
                # val > curr.val; go right
                if curr.right is None:
                    curr.right = node
                    return
                else:
                    curr = curr.right

    def get_smallest_node_value(self, root):
        curr = root
        while curr.left:
            curr = curr.left

        return curr

    def delete(self, val):
        return self.recursive_delete_node(self.head, val)

    def recursive_delete_node(self, root, val):
        """
        approach: recursively delete then rebalance the tree
        """
        # if not found, return not found
        if root is None:
            print(f'Node {val} not found.')
            return root

        if val < root.val:
            root.left = self.recursive_delete_node(root.left, val)
        elif val > root.val:
            root.right = self.recursive_delete_node(root.right, val)
        else:
            # Case1: leaf node
            if root.left is None and root.right is None:
                self.count -= 1
                return None

            # Case2: one child: test for one side and return the other side.
            if root.left is None:
                right = root.right
                root = None
                self.count -= 1
                return right
            elif root.right is None:
                left = root.left
                root = None
                self.count -= 1
                return left

            # Case3: two children, traverse inorder of right subtree to get smallest value.
            # Repeat delete with new value
            smallest_node = self.get_smallest_node_value(root.right)
            root.val = smallest_node.val
            root.right = self.recursive_delete_node(root.right, smallest_node.val)
        return root

    def get_tree_height(self):
        max_height = 1
        stack = [(self.head, 1)]
        while stack:
            pop, height = stack.pop()

            if pop.left or pop.right:
                if pop.left:
                    stack.append((pop.left, height + 1))
                if pop.right:
                    stack.append((pop.right, height + 1))
            else:
                max_height = max(max_height, height)

        return max_height

    """
    traversals
    """
    def print_nodes_level_order(self):
        q = [self.head]
        height = 1
        while q:
            curr_len = len(q)
            total_height = 'height ' + str(height) + ': '
            for item in range(curr_len):
                pop = q.pop(0)
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)

                if item == 0:
                    print(total_height, end='')
                # print on new line after the last node in the level
                if item == curr_len - 1:
                    print(pop.val)
                else:
                    print(pop.val, ', ',  end='')
            height += 1

    def print_nodes_inorder(self):
        curr = self.head
        stack = []

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                pop = stack.pop()
                print(str(pop.val), end='')

                if pop.right:
                    curr = pop.right

                # prettify the output
                if stack or curr:
                    print(', ', end='')

    def print_nodes_preorder(self):
        curr = self.head
        stack = []

        while curr or stack:
            if curr:
                print(curr.val, end='')
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            else:
                pop = stack.pop()
                print(pop.val, end='')

                if pop.right:
                   stack.append(pop.right)

                if pop.left:
                    curr = pop.left

            # prettify the output
            if curr or stack:
                print(', ', end='')

    def print_nodes_postorder(self):
        """
        Approach: iterative with one stack
        """
        curr = self.head
        stack = []

        while curr or stack:
            if curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            else:
                pop = stack.pop()
                top = stack[-1] if stack else None

                if pop.right and top == pop.right:
                    # remove the top item if its the same as the popped item
                    stack.pop()
                    curr = pop.right
                    stack.append(pop)
                else:
                    print(pop.val, end='')
                    curr = None

                # prettifies the output
                if not curr and stack:
                    print(', ', end='')




class BinarySearchTreeTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_insert(self):
        tree = BinarySearchTree()
        tree.insert(3)

        actual = 1
        expected = tree.count

        self.assertEqual(expected, actual, "should equal to Tree's count.")

    def test_multiple_insert(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        tree.print_nodes_level_order()
        actual_count = tree.count
        expected_count = len(data)
        print('total after insert: ', tree.count)
        self.assertEqual(actual_count, expected_count, 'total number of nodes should equal to data length')

    def test_delete_existing_value(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        tree.delete(15)
        tree.delete(10)
        tree.delete(3)
        tree.delete(6)
        tree.print_nodes_level_order()
        print('total after delete: ', tree.count)

        actual_count = tree.count
        expected_count = len(data) - 4
        self.assertEqual(actual_count, expected_count, 'total number of nodes should equal to data length minus number of deletions.')

    def test_delete_non_existing_value(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        actual_count = tree.count
        expected_count = 20

        tree.print_nodes_level_order()
        print('total before delete: ', actual_count)
        tree.delete(20)
        print('total after delete: ', actual_count)

        self.assertEqual(actual_count, expected_count, 'total number of nodes should remain the same.')

    def test_find_height(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        actual_height = tree.get_tree_height()
        expected_height = 5
        tree.print_nodes_level_order()
        self.assertEqual(actual_height, expected_height, 'height should be 5')

    def test_traverse_inorder(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        print('\ninorder: ')
        tree.print_nodes_inorder()

    def test_traverse_preorder(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        print('\npreorder: ')
        tree.print_nodes_preorder()

    def test_traverse_postorder(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        print('\npostorder: ')
        tree.print_nodes_postorder()
