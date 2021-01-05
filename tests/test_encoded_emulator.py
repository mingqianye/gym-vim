import unittest

import gym_vim
import numpy as np
from gym_vim.envs.encoded_emulator import *

class TestEncodedEmulator(unittest.TestCase):
    def setUp(self):
        self.e = EncodedEmulator("", "a", 3, 2, 
                all_keystrokes = ["a", "", " "],
                all_chars = ["a", "", " "])

    def tearDown(self):
        self.e.close()

    def test_reset(self):
        self.e.reset()

    def test_simple_input(self):
        encoded_action = self.e.encode_action("a")
        print(encoded_action)
        ob, reward, done, info = self.e.step(encoded_action)
        self.assertEqual(ob[1], 0)


if __name__ == '__main__':
    unittest.main()
