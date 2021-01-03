import unittest
import gym_vim
from gym_vim.envs.fs import *
from pynvim import attach

class TestVim(unittest.TestCase):
    def setUp(self):
        self.nvim = attach('child', argv=["/bin/env", "nvim", "--embed", "--headless"])

    def tearDown(self):
        self.nvim.close()

    def test_sh(self):
        self.assertEqual(["a"], sh("echo a"))
        self.assertRaises(Exception, sh, "blah")

    def test_simple(self):
        self.assertEqual(1, simple(self.nvim))

if __name__ == '__main__':
    unittest.main()
