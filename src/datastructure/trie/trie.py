import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node(None)
        self.count = 0


    def find(self, prefix: str) -> list:
        if len(prefix) == 0:
            return []

        p = self.root
        history = ''

        for w in prefix:
            if w in p.children:
                p = p.children[w]
                history += w
            else:
                return []

        results = self.find_all_paths(p, history)
        return results


    def find_all_paths(self, pointer, history) -> list:
        self.results = []

        for key, value in pointer.children.items():
            self.traverse(value, history)
        return self.results


    def traverse(self, root, history):
        if root is None:
            return None

        history = history + root.val
        if root.is_word:
            self.results.append(history)

        for key, value in root.children.items():
            self.traverse(value, history)


    def insert(self, word: str) -> bool:
        if len(word) == 0 or not word.isalpha():
            return False

        p = self.root
        for w in word:
            if w not in p.children:
                p.children[w] = Node(w)
            p = p.children[w]

        p.is_word = True
        self.count += 1
        return p.is_word



class TestTrie(unittest.TestCase):
    def setUp(self) -> None:
        self.trie = Trie()

    def test_find(self):
        trie = Trie()
        words = ['cat', 'call', 'catch']
        for w in words:
            trie.insert(w)

        letters = 'ca'
        actual = len(trie.find(letters))

        self.assertEqual(actual, 3, 'should return 3 words')
        self.assertEqual(sorted(words), sorted(trie.find(letters)), 'list should equal')

    def test_insert(self):
        trie = Trie()
        words = ['cat', 'call', 'catch', 'dog', 'doing', 'do', 'dong']
        for w in words:
            trie.insert(w)

        actual = trie.count
        expected = len(words)
        self.assertEqual(actual, expected, "should equal")

    def test_get_all_words_related_to_string(self):
        trie = Trie()
        words = ['cat', 'call', 'catch', 'dog', 'doing', 'do', 'dong']
        for w in words:
            trie.insert(w)

        letters = 'ca'
        actual = len(trie.find(letters))
        expected = 3

        self.assertEqual(actual, expected, "should find 3 words from 'ca'")

    def test_insert_corner_cases(self):
        trie = Trie()
        words = ['', ' ', '@!#', '3 4']
        for w in words:
            trie.insert(w)
        actual = trie.count
        expected = 0
        self.assertEqual(actual, expected, "should equal to: ")

    # corner cases for trie.find
    def test_find_with_blank_space(self):
        trie = Trie()
        words = ['cat', 'call', 'catch', 'dog', 'doing', 'do', 'dong']
        for w in words:
            trie.insert(w)

        string = ' '
        actual = trie.find(string)
        expected = []

        self.assertEqual(actual, expected, "should return empty array")

    def test_find_with_empty_string(self):
        trie = Trie()
        words = ['cat', 'call', 'catch', 'dog', 'doing', 'do', 'dong']
        for w in words:
            trie.insert(w)

        string = ''
        actual = trie.find(string)
        expected = []

        self.assertEqual(actual, expected, "should return empty array")

    def test_find_with_special_characters(self):
        trie = Trie()
        words = ['cat', 'call', 'catch', 'dog', 'doing', 'do', 'dong']
        for w in words:
            trie.insert(w)

        string = 'ca#'
        actual = trie.find(string)
        expected = []

        self.assertEqual(actual, expected, "should return empty array ")

    def test_find_with_string_and_integers(self):
        trie = Trie()
        words = ['cat', 'call', 'catch', 'dog', 'doing', 'do', 'dong']
        for w in words:
            trie.insert(w)

        string = 'c6a'
        actual = trie.find(string)
        expected = []
        self.assertEqual(actual, expected, "should return empty array")



if __name__== "__main__":
    unittest.main()
