import unittest

import gym_vim
import numpy as np
from gym_vim.envs.emulator import *

class TestEmulator(unittest.TestCase):
    def setUp(self):
        self.e = Emulator(["ham"])

    def tearDown(self):
        self.e.close()

    def test_start_stop(self):
        self.e.reset()

    def test_simple_input(self):
        ob, reward, done, info = self.e.step("i")
        self.assertEqual(ob.last_action, "i")
        self.assertEqual(reward, 0)
        self.assertEqual(done, False)
        self.assertEqual(info, {})


if __name__ == '__main__':
    unittest.main()
