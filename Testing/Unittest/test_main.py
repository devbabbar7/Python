import unittest
import main1

class Test_Add(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main1.add(1,2),3)
        self.assertEqual(main1.add(6,7),13)
        
if __name__ == '__main__':
    unittest.main()