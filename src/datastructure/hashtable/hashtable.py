import unittest

class Node:
    def __init__(self, key: str, val: str):
        self.val = val
        self.key = key
        self.next = None


class HashTable:
    def __init__(self):
        self.buckets = [None] * 3
        self.size = 0

    def get_hash(self, key: str) -> int:
        count = 0
        for s in key:
            count += ord(s)

        # mod 3 is arbitrarily chosen
        bucket = count % 3
        return bucket

    def search(self, key: str) -> str:
        bucket = self.get_hash(key)

        head = self.buckets[bucket]
        while head:
            if key == head.key:
                return head.val
            else:
                head = head.next
        return None
            

    def insert(self, key: str, val: str) -> bool:
        if len(val) == 0:
            return False
        # get bucket through get_hash
        bucket = self.get_hash(key)
        # if bucket is None, create node, place in bucket, return
        node = Node(key, val)
        if self.buckets[bucket] is None:
            self.buckets[bucket] = node
        else:
            # if bucket contains something, traverse through the LL until the end, create node, and attach to tail next
            head = self.buckets[bucket]
            
            while head.next is not None:
                if head.key == key:
                    head.val = val
                    return True
                head = head.next
            head.next = node
        self.size += 1
        return True

    def delete(self, key: str) -> str:
        bucket = self.get_hash(key)
        head = self.buckets[bucket]

        prev = None
        while head:
            if key == head.key:
                # deletion at head
                if prev is None:
                    self.buckets[bucket] = head.next
                    self.size -= 1
                    return head.val
                elif prev:
                    prev.next = head.next
                    self.size -= 1
                    return head.val
                else:
                    # deletion at tail
                    prev.next = None
                    self.size -= 1
                    return head.val
            prev = head
            head = head.next


        return None


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash = HashTable()

    def test_get_hash(self):
        self.hash.get_hash('a')
        self.hash.get_hash('b')
        self.hash.get_hash('c')
        self.hash.get_hash('d')
        self.hash.get_hash('kevin')
        self.hash.get_hash('kevin')

        self.assertEqual(self.hash.get_hash('a'), 1, 'should equal to')
        self.assertEqual(self.hash.get_hash('b'), 2, 'should equal to')
        self.assertEqual(self.hash.get_hash('c'), 0, 'should equal to')
        self.assertEqual(self.hash.get_hash('d'), 1, 'should equal to')
        self.assertEqual(self.hash.get_hash('kevin'), 1, 'should equal to')
        self.assertEqual(self.hash.get_hash('kevin'), self.hash.get_hash('kevin'), 'hashing string twice should be consistent')

    def test_insert(self):
        hash = HashTable()
        hash.insert('a', '1')
        hash.insert('b', '2')
        hash.insert('c', '3')
        hash.insert('d', '4')
        hash.insert('kevin', 'kevin')
        hash.insert('a', '5')

        expected = 5
        actual = hash.size
        self.assertEqual(expected, actual, 'should equal to size.')
        self.assertEqual(hash.search('a'), '5', 'overriding existing key should equal to new value')

    def test_search(self):
        hash = HashTable()
        hash.insert('a', '1')
        hash.insert('b', '2')
        hash.insert('c', '3')
        
        hash.search('a')
        hash.search('b')
        hash.search('c')       
        
        self.assertEqual(hash.search('a'), '1', 'should return value')
        self.assertEqual(hash.search('b'), '2', 'should return value')
        self.assertEqual(hash.search('c'), '3', 'should return value')

    def test_delete_at_head(self):
        hash = HashTable()
        hash.insert('a', '1')
        hash.insert('d', '4')
        actual = hash.delete('a')

        # delete a: return 1
        self.assertEqual('1', actual, "deleted key should return deleted key's value")

        new_head = hash.buckets[hash.get_hash('a')].val
        self.assertEqual(new_head, '4', "after deletion of a linked list with 2 elements, the remaining element should be the head")

        new_size = hash.size
        self.assertEqual(new_size, 1, "total elements after deletion should equal to 1")

    def test_delete_at_tail(self):
        hash = HashTable()
        hash.insert('a', '1')
        hash.insert('b', '2')
        hash.insert('c', '3')
        actual = hash.delete('c')

        # delete c: return 3
        self.assertEqual('3', actual, "deleted key should return deleted key's value")

        new_size = hash.size
        self.assertEqual(new_size, 2, "total elements after deletion should equal to 2")
