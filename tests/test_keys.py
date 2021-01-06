import unittest
from gym_vim.envs.keys import chars
class TestKeys(unittest.TestCase):
    def test_keystrokes(self):
        self.assertEqual(True, len(chars) > 0)
