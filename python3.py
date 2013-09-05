#!/usr/bin/env python

import unittest

class Test3(unittest.TestCase):
    def test_tuple(self):
        # tuples are fixed-length collections
        a, b, c = (1, 2, "Foo")
        self.assertEquals(a, 1)
        self.assertEquals(b, 2)
        self.assertEquals(c, 'Foo')

    def test_list(self):
        # list can be any length and are mutable
        x = []
        self.assertEquals(len(x), 0)
        x.append(1)
        self.assertEquals(len(x), 1)
        self.assertEquals(x[0], 1)
        x.append(2)
        self.assertEquals(len(x), 2)
        self.assertEquals(x[1], 2)
        self.assertEquals(x[-1], 2)
        self.assertTrue(1 in x)

        y = [i for i in range(5)]
        self.assertEquals(y, [0,1,2,3,4])
        z = [i for i in range(10) if i % 3 == 0]
        self.assertEquals(z, [0,3,6,9])
        self.assertEquals(z[0:2], [0,3])

    def test_dict(self):
        # dict map keys to other objects and are also mutable
        x = {}
        self.assertEquals(len(x), 0)
        x['foo'] = 0
        self.assertEquals(x['foo'], 0)
        def bad():
            return x['bar']
        self.assertRaises(KeyError, bad)
        self.assertEquals(x.get('bar', ''), '')
            
if __name__ == '__main__':
    unittest.main()
