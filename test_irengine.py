import unittest
import irengine as test

class TestIREngine(unittest.TestCase):

    def test_tokenize(self):
        """returns TOKENS if passed a str, raises exception otherwise."""
        string = "how now brown crown"
        self.assertEqual(test.tokenize(string), 
                         ["how", "now", "brown", "crown"])
        with self.assertRaises(TypeError):
            test.tokenize(True)
            test.tokenize(1)
            test.tokenize(["True", "1"])

    def test_normalize(self):
        """returns NORMALIZED tokens."""
        self.assertEqual(test.normalize("Test"), "test")
        self.assertEqual(test.normalize("test"), "test")


if __name__ == "__main__":
    unittest.main()