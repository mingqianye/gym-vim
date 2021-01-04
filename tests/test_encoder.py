import unittest

import gym_vim
import numpy as np
from gym_vim.envs.encoder import *

class TestEncoder(unittest.TestCase):
    def test_encode(self):
        encoder = Encoder(["a", "b"])
        self.assertEqual(2, encoder.size())
        arr1 = encoder.encode("a")
        self.assertEqual([1, 0], [arr1[0], arr1[1]])
        arr2 = encoder.encode("b")
        self.assertEqual([0, 1], [arr2[0], arr2[1]])

    def test_decode(self):
        encoder = Encoder(["a", "b"])
        self.assertEqual("a", encoder.decode(np.array([1,0])))
        self.assertEqual("a", encoder.decode(np.array([0.9,0])))
        self.assertEqual("b", encoder.decode(np.array([0,0.9])))

if __name__ == '__main__':
    unittest.main()
