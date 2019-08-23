import unittest

from tests_helper import call_module


class TestCase(unittest.TestCase):
    def test_hello_world(self):
        results = call_module(self, 1)
        self.assertEqual(results[0], "Hello, World!")
