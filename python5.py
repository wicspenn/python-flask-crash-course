#!/usr/bin/env python

import unittest

class Test5(unittest.TestCase):
    def test_import(self):
        import re
        from re import match
        self.assertEquals(re.match, match)
        import python4
        x = python4.Foo(1)
        self.assertEquals(x.value, 1)

if __name__ == '__main__':
    unittest.main()
