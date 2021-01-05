import unittest

import gym_vim
import numpy as np
from gym_vim.envs.edit_distance import *

class TestEditDistance(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(edit_distance("", ""), 0)
        self.assertEqual(edit_distance("a", "a"), 0)
        self.assertEqual(edit_distance("a", ""), 1)
        self.assertEqual(edit_distance("a", "ab"), 1)
        self.assertEqual(edit_distance("aB", "ab"), 1)
        self.assertEqual(edit_distance("ab", "ab"), 0)
        self.assertEqual(edit_distance("ab", "abc"), 1)
        self.assertEqual(edit_distance("ab C", "ab cd"), 2)
        self.assertEqual(edit_distance("ab c", "efg"), 4)

    def test_arr_distance(self):
        self.assertEqual(arr_edit_distance(["a","a"], ["ab","a"]), 1)


if __name__ == '__main__':
    unittest.main()
