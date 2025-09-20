import unittest
from mathfuns import isprime, gcd, isperfect

class TestMathFuns(unittest.TestCase):
    def test_isprime(self):
        self.assertFalse(isprime(0))
        self.assertFalse(isprime(1))
        self.assertTrue(isprime(2))
        self.assertTrue(isprime(3))
        self.assertFalse(isprime(4))
        self.assertTrue(isprime(13))
        self.assertFalse(isprime(15))
        self.assertTrue(isprime(97))
        self.assertFalse(isprime(-7))

    def test_gcd(self):
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(100, 10), 10)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(270, 192), 6)

    def test_isperfect(self):
        self.assertFalse(isperfect(0))
        self.assertFalse(isperfect(1))
        self.assertTrue(isperfect(6))    # 1 + 2 + 3 = 6
        self.assertTrue(isperfect(28))   # 1 + 2 + 4 + 7 + 14 = 28
        self.assertFalse(isperfect(12))
        self.assertFalse(isperfect(27))
        self.assertTrue(isperfect(496))
        self.assertFalse(isperfect(-6))

if __name__ == "__main__":
    unittest.main()