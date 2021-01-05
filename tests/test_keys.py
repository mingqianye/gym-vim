import unittest
from gym_vim.envs.keys import keystrokes
class TestKeys(unittest.TestCase):
    def test_keystrokes(self):
        self.assertEqual(94, len(keystrokes))
