import unittest
import irengine as test

class TestIREngine(unittest.TestCase):

    def test_tokenize(self):
        """return TOKENS if passed a str, raises exception otherwise."""
        string = "how now brown crown"
        self.assertEqual(test.tokenize(string), 
                         ["how", "now", "brown", "crown"])

if __name__ == "__main__":
    unittest.main()