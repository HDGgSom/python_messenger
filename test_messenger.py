from utils import bytes_to_dict, dict_to_bytes
import unittest

message = {
    'user': 'gSom',
    'action': 'presence'
}

bmessage = dict_to_bytes(message)


class TestDictToBytes(unittest.TestCase):

    def test_dict_to_bytes(self):
        self.assertEqual(type(dict_to_bytes(message)), bytes)

class TestBytesToDict(unittest.TestCase):

    def test_bytes_to_dict(self):
        self.assertEqual(type(bytes_to_dict(bmessage)), dict)

if __name__ == '__main__':
    unittest.main()