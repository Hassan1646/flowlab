import unittest
from app import greet, farewell

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Hassan"), "Hello, Hassan!")

if __name__ == "__main__":
    unittest.main()

class TestFarewell(unittest.TestCase):
    def test_farewell(self):
        self.assertEqual(farewell("Hassan"), "Goodbye, Hassan!")