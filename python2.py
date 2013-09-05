#!/usr/bin/env python

import unittest

class Test2(unittest.TestCase):
    def test_conditionals(self):
        if True:
            pass
        else:
            self.fail("False is not True")

    def test_loops(self):
        i = 0
        while i < 10:
            self.assertTrue(i < 10)
            i += 1
        for i in range(10):
            self.assertTrue(0 <= i < 10)

    def test_functions(self):
        def plus_one(n):
            return n + 1
        self.assertEquals(plus_one(0), 1)
        def plus_one2(n=0):
            return plus_one(n)
        self.assertEquals(plus_one2(), 1)
        self.assertEquals(plus_one2(n=5), 6)

    def test_exceptions(self):
        def raises_exception():
            raise Exception("exception")
        self.assertRaises(Exception, raises_exception)
        try:
            raises_exception()
        except Exception as e:
            self.assertEquals(e.message, "exception")

            
if __name__ == '__main__':
    unittest.main()
