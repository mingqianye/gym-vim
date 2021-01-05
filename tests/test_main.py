import unittest
import gym

class TestVim(unittest.TestCase):
    def test_env(self):
        env = gym.make("vim-v0")
        env.render()

    def test_hello(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
