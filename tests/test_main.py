import unittest
import gym

import gym_vim

class TestVim(unittest.TestCase):
    #def test_env(self):
    #    env = gym.make("Vim-v0")
    #    env.reset()
    #    env.step(0)

    def test_hello(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
