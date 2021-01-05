import logging
from gym_vim.envs.vim_env import VimEnv
from gym.envs.registration import register


logger = logging.getLogger(__name__)
register(id="Vim-v0", entry_point="gym_vim.envs:VimEnv")
