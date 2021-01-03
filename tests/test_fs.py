import unittest
import gym_vim
from gym_vim.envs.fs import *

class TestVim(unittest.TestCase):
    def test_sh(self):
        self.assertEqual(b"a\n", sh("echo a"))
        self.assertRaises(Exception, sh, "blah")

if __name__ == '__main__':
    unittest.main()
