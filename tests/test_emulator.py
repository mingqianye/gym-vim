import unittest

import gym_vim
import numpy as np
from gym_vim.envs.emulator import *

class TestEmulator(unittest.TestCase):
    def setUp(self):
        self.e = Emulator("spam", "ham", 30)

    def tearDown(self):
        self.e.close()

    def test_reset(self):
        self.e.reset()

    def test_simple_input(self):
        ob, reward, done, info = self.e.step("i")
        self.assertEqual(ob.last_action, "i")
        self.assertEqual(ob.mode, "i")
        self.assertEqual(ob.curpos, [0, 1, 1, 0, 1])
        self.assertEqual(ob.string, "spam")
        self.assertEqual(reward, -1)
        self.assertEqual(done, False)

    def test_simple_input2(self):
        ob, reward, done, info = self.e.step("x")
        ob, reward, done, info = self.e.step("x")
        ob, reward, done, info = self.e.step("i")
        ob, reward, done, info = self.e.step("h")
        self.assertEqual(ob.last_action, "h")
        self.assertEqual(ob.mode, "i")
        self.assertEqual(ob.curpos, [0, 1, 2, 0, 2])
        self.assertEqual(ob.string, "ham")
        self.assertEqual(reward, 100)
        self.assertEqual(done, True)

if __name__ == '__main__':
    unittest.main()
