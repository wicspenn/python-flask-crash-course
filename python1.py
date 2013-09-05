#!/usr/bin/env python

import unittest

class Test1(unittest.TestCase):
    def test_literals(self):
        # booleans
        self.assertTrue(True)
        self.assertTrue(not False)
        self.assertTrue(True or False)
        self.assertFalse(True and False)

        # there is also a special value None
        n = None
        self.assertTrue(n is None) # reference equality
    
    def test_numbers(self):
        # int should be familiar
        self.assertEqual(1 + 1, 2)
        i = 1
        self.assertEqual(i - 1, int(0))
        self.assertEqual(1 * 2, 2)
        self.assertEqual(5 % 3, 2)

        # Division is a little weird...
        self.assertEqual(1 / 2, 0)

        # float to the rescue!
        self.assertEqual(1 / float(2), 0.5)
        self.assertEqual(1 // 2.0, 0)

    def test_strings(self):
        self.assertNotEqual('foo', "bar")
        x = """Hello.
World."""
        self.assertEqual(x, "Hello.\n%s." % "World")
        self.assertEqual(len('foo'), 3)

if __name__ == '__main__':
    unittest.main()
