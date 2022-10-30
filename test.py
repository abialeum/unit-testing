import unittest  
class TestingSum(unittest.TestCase):  

    def getAction(self,action):
        if action == 'hungry':
            return 'go to eat'
        elif action == 'sleepy':
            return 'go to sleep'
        
    def test_sum(self):  
        self.assertEqual(sum([1, 4, 5]), 10, "It should be 10")  
        self.assertEqual(10-5, 5, "It should be 5")  
    
    def test_getAction(self):
        self.assertEqual(self.getAction('hungry'),'go to eat', "It should be 'go to eat'")
        self.assertEqual(self.getAction('sleepy'),'go to sleep', "It should be 'go to sleep'")
  
if __name__ == '__main__':  
    unittest.main()