import unittest


class Graph:

    def __init__(self):
        self.graph = {}

    def insert(self, value: int, connections: list):
        self.graph[value] = connections

    def is_connected(self, node1: int, node2: int) -> bool:
        if node1 in self.graph:
            return node2 in self.graph[node1]
        return False


class TestGraph(unittest.TestCase):
    """
    0 - 1 - 2
    | / | . |
    4 - 3 ---
    """

    def test_insert(self):
        node0 = [1, 4]
        node1 = [2, 3, 4]
        node2 = [1, 3]
        node3 = [1, 2, 4]
        node4 = [0, 1, 3]

        graph = Graph()
        graph.insert(0, node0)
        graph.insert(1, node1)
        graph.insert(2, node2)
        graph.insert(3, node3)
        graph.insert(4, node4)

        actual1 = graph.is_connected(1, 3)
        self.assertEqual(True, actual1, "node1 and node3 should be connected, but {} was returned.".format(actual1))

        actual2 = graph.is_connected(4, 2)
        self.assertEqual(False, actual2, "node 4 and 2 should not be connected, but {} was returned.".format(actual2))


if __name__ == "__main__":
    unittest.main(verbosity=3)