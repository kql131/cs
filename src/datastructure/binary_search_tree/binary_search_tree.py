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

    def get_max_tree_height(self):
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

    def search(self, val):
        if self.head is None:
            return False

        curr = self.head
        while curr:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    print(f'Node {val} not found.')
                    return False
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    print(f'Node {val} not found')
                    return False
            else:
                return curr

    def is_balanced(self):
        if self.head is None:
            return False

        left = self.find_tree_height(self.head.left)
        right = self.find_tree_height(self.head.right)

        return False if abs(left - right) > 1 else True

    def find_tree_height(self, root):
        if root is None:
            return 0

        left = self.find_tree_height(root.left)
        right = self.find_tree_height(root.right)

        return max(left, right) + 1

    def balance_the_tree(self):
        if self.is_balanced():
            return True

        # find which side is lopsided
        left_subtree = self.find_tree_height(self.head.left)
        right_subtree = self.find_tree_height(self.head.right)

        # compare left > right or left < right
        if left_subtree > right_subtree and abs(left_subtree - right_subtree) > 1:
            # go into left and get the next largest node
            next_largest = self.get_largest_node(self.head.left)
            val = next_largest.val

            node = Node(val)
            node.left = self.head.left
            node.right = self.head

            # before updating head to the new node, disconnect head's left pointer
            self.head.left = None
            self.head = node
            node.left = self.recursive_delete_node(node.left, val)

        elif right_subtree > left_subtree and abs(left_subtree - right_subtree) > 1:
            # go into right and get the next smallest node
            next_smallest = self.get_smallest_node_value(self.head.right)
            val = next_smallest.val

            node = Node(val)
            node.left = self.head
            node.right = self.head.right

            # before updating head to point to the new node, disconnect head's right pointer
            self.head.right = None
            self.head = node
            node.right = self.recursive_delete_node(node.right, val)

        return self.balance_the_tree()

    def get_largest_node(self, root):
        curr = root

        while curr.right:
            curr = curr.right

        return curr

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
        expected_count = 10

        tree.print_nodes_level_order()
        print('total before delete: ', actual_count)
        tree.delete(20)
        print('total after delete: ', actual_count)

        self.assertEqual(actual_count, expected_count, 'total number of nodes should remain the same.')

    def test_find_max_tree_height(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        actual_height = tree.get_max_tree_height()
        expected_height = 5
        tree.print_nodes_level_order()
        self.assertEqual(actual_height, expected_height, 'height should be 5')

    def test_search_for_existing_value(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        actual = tree.search(14).val
        expected = 14
        self.assertEqual(actual, expected, "function should return the matched Node's value")

    def test_search_for_non_existing_value(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        actual = tree.search(22)
        expected = False
        self.assertEqual(actual, expected, "should return False because value doens't exist in tree.")

    def test_tree_is_balanced(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        actual = tree.is_balanced()
        expected = False
        self.assertEqual(actual, expected, 'should return False because tree height is not balanced')

    def test_balance_the_tree(self):
        tree = BinarySearchTree()
        data = [10, 6, 3, 8, 15, 12, 13, 14, 18, 19]
        for d in data:
            tree.insert(d)

        tree.print_nodes_level_order()

        tree.balance_the_tree()
        tree.print_nodes_level_order()

    def test_balance_degenerate_tree(self):
        tree = BinarySearchTree()
        data = [5, 4, 3, 2, 1]
        for d in data:
            tree.insert(d)

        tree.print_nodes_level_order()
        tree.balance_the_tree()
        tree.print_nodes_level_order()

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
