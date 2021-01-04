import pynvim

from typing import NewType, List, Tuple, Dict
from dataclasses import dataclass
from gym_vim.envs.fs import get_state

EmulatorAction = NewType("EmulatorAction", str)
NvimMode=NewType("NvimMode", str)

@dataclass(eq=True, frozen=True)
class EmulatorState:
    last_action: EmulatorAction
    mode: NvimMode
    curpos: List[int]
    strings: List[str]

class Emulator:
    _nvim: pynvim.api.nvim.Nvim
    _target_strings: List[str]

    def __init__(self, target_strings: List[str]):
        self._nvim = Emulator._new_nvim_instance()
        self._target_strings = target_strings

    def step(self, action: EmulatorAction) -> Tuple[EmulatorState, int, bool, Dict]:
        self._nvim.feedkeys(action)
        vimstate = get_state(self._nvim)
        return EmulatorState(
                action,
                vimstate.mode,
                vimstate.curpos,
                vimstate.strings
        ), 0, False, {}


    def reset(self):
        self._nvim.quit()
        self._nvim.close()
        self._nvim = Emulator._new_nvim_instance()

    def render(self, mode='human') -> None:
        print("some debug info here")

    def close(self):
        self._nvim.quit()
        self._nvim.close()

    def _new_nvim_instance():
        return pynvim.attach('child', argv=["/bin/env", "nvim", "--embed", "--headless", "--noplugin", "--clean", "-n"])
