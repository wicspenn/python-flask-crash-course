#!/usr/bin/env python

import unittest

class Foo:
    def __init__(self, value):
        self.value = value
    
    def foo(self):
        return self.value

class Bar(Foo):
    def foo(self):
        return self.value + 1

    def bar(self):
        return self.value

class Test4(unittest.TestCase):
    def setUp(self):
        self.foo = Foo(1)
        self.bar = Bar(1)

    def test_Foo(self):
        self.assertEquals(self.foo.foo(), 1)
        def raises_NameError():
            self.foo.bar()
        self.assertRaises(AttributeError, raises_NameError)

    def test_Bar(self):
        self.assertEquals(self.bar.foo(), 2)
        self.assertEquals(self.bar.bar(), 1)
        
if __name__ == '__main__':
    unittest.main()
