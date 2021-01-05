import numpy as np
from gym_vim.envs.emulator import Emulator, EmulatorState, ScreenString, EmulatorAction
from gym_vim.envs.encoder import Encoder
from gym_vim.envs.keys import keystrokes, displayable_chars, modes

from typing import NewType, Tuple, Dict, List

EncodedObservation = NewType("EncodedObservation", np.ndarray)

class EncodedEmulator:
    def __init__(self, 
            start_string: str, 
            target_string: str, 
            max_steps: int, 
            max_string_len: int,
            all_keystrokes: List[str] = keystrokes,
            all_chars: List[str] = displayable_chars,
            all_modes: List[str] = modes
            ):
        self._emulator: Emulator = Emulator(start_string, target_string, max_steps)
        self._action_encoder: Encoder = Encoder(all_keystrokes)
        self._char_encoder: Encoder = Encoder(all_chars)
        self._mode_encoder: Encoder = Encoder(all_modes)
        self._max_string_len: int = max_string_len
        
    def step(self, encoded_action) -> Tuple[EncodedObservation, int, bool, Dict]:
        ob, reward, done, info = self._emulator.step(
                self._action_encoder.decode(encoded_action))

        return self.__encode_ob(ob), reward, done, info

    def reset(self):
        self._emulator.reset()

    def render(self):
        self._emulator.render()

    def close(self):
        self._emulator.close()

    def encode_action(self, action: EmulatorAction) -> np.ndarray:
        return self._action_encoder.encode(action)

    def __encode_ob(self, ob: EmulatorState) -> EncodedObservation:
        return np.concatenate([
                self.encode_action(ob.last_action),
                self._mode_encoder.encode(ob.mode),
                ob.curpos,
                self.__encode_string(ob.string)
        ])

    def __encode_string(self, s: ScreenString) -> np.ndarray:
        arrs = []
        for c in s.ljust(self._max_string_len):
            arrs.append(self._char_encoder.encode(c))
        return np.concatenate(arrs)
