import pynvim

from typing import NewType, List, Tuple, Dict
from dataclasses import dataclass
from gym_vim.envs.fs import get_state, is_valid, feedkeys, VimState
from gym_vim.envs.edit_distance import edit_distance
from gym_vim.envs.keys import esc

EmulatorAction = NewType("EmulatorAction", str)
NvimMode = NewType("NvimMode", str)
ScreenString = NewType("NvimScreenString", str)

@dataclass(eq=True, frozen=True)
class EmulatorState:
    last_action: EmulatorAction
    mode: NvimMode
    curpos: List[int]
    string: ScreenString

class NvimWrapper:
    def __init__(self, start_string: ScreenString):
        self._nvim: pynvim.api.nvim.Nvim = NvimWrapper.__new_nvim_instance(start_string)
        self._state_string: ScreenString = start_string

    def inital_state(self) -> EmulatorState:
        return NvimWrapper.__state_with_action(self._nvim, "")

    def send_action(self, action: EmulatorAction) -> EmulatorState:
        feedkeys(self._nvim, action)
        return NvimWrapper.__state_with_action(self._nvim, action)

    def __state_with_action(nvim: pynvim.api.nvim.Nvim, action: EmulatorAction) -> EmulatorState:
        vimstate = get_state(nvim)
        return EmulatorState(
                action,
                vimstate.mode,
                vimstate.curpos,
                "".join(vimstate.strings))

    def __new_nvim_instance(start_string: ScreenString) -> pynvim.api.nvim.Nvim:
        nvim = pynvim.attach('child', argv=["/bin/env", "nvim", "--embed", "--headless", "--noplugin", "--clean", "-n"])
        feedkeys(nvim, "i")
        feedkeys(nvim, start_string)
        feedkeys(nvim, esc)
        feedkeys(nvim, "gg")
        return nvim
    
    def is_valid(self):
        return is_valid(self._nvim)

    def close(self):
        self._nvim.quit()
        self._nvim.close()

    def reset(self):
        self.close()
        self._nvim = NvimWrapper.__new_nvim_instance(self._state_string)

class Emulator:
    def __init__(self, start_string: ScreenString, target_string: ScreenString, max_steps: int):
        self._nvim: NvimWrapper = NvimWrapper(start_string)
        self._emulator_states: List[EmulatorState] = [self._nvim.inital_state()]
        self._target_string: ScreenString = target_string
        self._max_steps: int = max_steps

    def step(self, action: EmulatorAction) -> Tuple[EmulatorState, int, bool, Dict]:
        self._emulator_states.append(self._nvim.send_action(action))

        reward = self.__reward()
        done = self.__is_done()
        info = {}

        return self._emulator_states[-1], reward, done, info

    def __reward(self):
        prev_distance = edit_distance(
            self._emulator_states[-2].string,
            self._target_string)

        new_distance = edit_distance(
            self._emulator_states[-1].string,
            self._target_string)

        if new_distance == 0:
            return 100
        if new_distance == prev_distance:
            return -1
        if new_distance > prev_distance:
            return -10
        if new_distance < prev_distance:
            return 10

    def __is_done(self):
        return self._emulator_states[-1].string == self._target_string \
                or len(self._emulator_states) >= self._max_steps \
                or not self._nvim.is_valid()

    def reset(self):
        self._nvim.reset()
        self._emulator_states = [self._nvim.inital_state()]

    def render(self) -> None:
        print(self._emulator_states[-1])

    def close(self):
        self._nvim.close()
