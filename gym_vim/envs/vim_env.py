import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_vim.envs.encoded_emulator import EncodedEmulator

class VimEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.emulator = EncodedEmulator("abc", "a c", 4, 5)
        self.action_space = self.emulator.action_space()
        self.observation_space = self.emulator.observation_space()

    def step(self, action):
        return self.emulator.step(action)

    def reset(self):
        return self.emulator.reset()

    def render(self, mode='human') -> None:
        print("Rendering...")
        self.emulator.reset()

    def close(self):
        self.emulator.close()
