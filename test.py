import unittest  
class TestingSum(unittest.TestCase):  

    def test_sum(self):  
        self.assertEqual(sum([1, 4, 5]), 10, "It should be 10")  

  
if __name__ == '__main__':  
    unittest.main()