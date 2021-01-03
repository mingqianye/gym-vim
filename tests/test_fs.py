import unittest
import gym_vim
from gym_vim.envs.fs import *

class TestVim(unittest.TestCase):
    def test_sh(self):
        self.assertEqual(["a"], sh("echo a"))
        self.assertRaises(Exception, sh, "blah")

    def test_tt(self):
        self.assertEqual("blah", tt())

if __name__ == '__main__':
    unittest.main()
