
import unittest
import capital

class testPrimeNumber(unittest.TestCase):
    def testOne(self):
        result = capital.capText("Nate")
        self.assertEqual(result,"Nate") 
    def testSecond(self):
        result = capital.capText("this is a text string to test the unittest on a file")
        self.assertEqual(result,"This Is A Text String To Test The Unittest On A File")
        
if __name__ == "__main__":
    unittest.main()
