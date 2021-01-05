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
        ob, reward, done, info = self.e.step(encoded_action)

    def test_action_space(self):
        self.assertEqual(True, 0 <= self.e.action_space().sample() <= 2)

    def test_observation_space(self):
        self.assertEqual(43, self.e.observation_space().sample().size)

if __name__ == '__main__':
    unittest.main()
