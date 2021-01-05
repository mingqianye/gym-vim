from gym.envs.registration import register
from gym_vim.envs.vim_env import VimEnv

register(id='vim-v0', entry_point='gym_vim.envs:VimEnv')
