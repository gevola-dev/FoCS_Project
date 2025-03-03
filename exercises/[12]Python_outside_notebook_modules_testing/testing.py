import utils
import unittest

class TestClass(unittest.TestCase):
    
    def test_create_list(self):
        self.assertEqual(utils.create_list(2, 4), [2, 2, 2, 2])
        self.assertEqual(utils.create_list(2, 0), [])

    def test_create_dict(self):
        keys_values = (('a', 3), ('b', 2), ('c', 3), ('d', 15), ('e', 1))
        expected_output = {'a' : 3,
                           'b':  2,
                           'c' : 3,
                           'd' : 15,
                           'e' : 1}
        self.assertEqual(utils.create_dict(keys_values), expected_output)
    
    def test_append_element_to_list(self):
        a = utils.append_element_to_list(1)
        self.assertEqual(a, [1])
        
        b = utils.append_element_to_list(2, a)
        self.assertEqual(b, [1, 2])
        
        c = utils.append_element_to_list(3, b)
        self.assertEqual(c, [1, 2, 3])
        
        d = utils.append_element_to_list(4)
        self.assertEqual(d, [4])
                
        e = utils.append_element_to_list(5, a)
        self.assertEqual(e, [1, 5])

unittest.main(argv=[''], verbosity=2, exit=False)