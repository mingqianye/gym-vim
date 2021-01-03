import gym
from gym import error, spaces, utils
from gym.utils import seeding

class VimEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        ...
    def step(self, action):
        ...
    def reset(self):
        ...

    def render(self, mode='human') -> None:
        print("some debug info here")

    def close(self):
        ...
