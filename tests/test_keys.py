import unittest
from gym_vim.envs.keys import keystrokes
class TestKeys(unittest.TestCase):
    def test_keystrokes(self):
        self.assertEqual(93, len(keystrokes))
