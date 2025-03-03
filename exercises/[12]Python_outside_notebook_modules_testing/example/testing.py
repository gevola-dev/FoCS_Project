import utils
import unittest

class TestUtils(unittest.TestCase):
    
    def test_email(self):
        # "simone@gmail.com" = TRUE
        self.assertTrue(utils.controlla_email("simone@gmail.com"))

        # "@gmail.it" = FALSE
        self.assertFalse(utils.controlla_email("@gmail.it"))

        # "simone1@gmail.com" = TRUE
        self.assertTrue(utils.controlla_email("simone1@gmail.com"))

    def test_somma_vettori(self):
        # "1 2 3 4 5" = 15
        self.assertEqual(utils.somma_vettore([1,2,3,4,5]), 15)

        # "a" = 0
        self.assertEqual(utils.somma_vettore([]), 0)

if __name__ == "__main__":
    unittest.main()