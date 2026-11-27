import unittest
from app import greet, farewell

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Hassan"), "Hi, Hassan!")
    def test_empty_name(self):
        self.assertEqual(greet(""), "Hi, friend!")

    def test_custom_greeting(self):
        self.assertEqual(greet("Hassan", "Hey"), "Hey, Hassan!")

class TestFarewell(unittest.TestCase):
    def test_farewell(self):
        self.assertEqual(farewell("Hassan"), "Goodbye, Hassan!")

if __name__ == "__main__":
    unittest.main()