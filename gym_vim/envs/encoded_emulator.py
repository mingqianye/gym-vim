import numpy as np
from gym_vim.envs.emulator import Emulator, EmulatorState, ScreenString, EmulatorAction
from gym_vim.envs.encoder import Encoder
from gym_vim.envs.action_encoder import ActionEncoder
from gym_vim.envs.keys import chars, modes

from gym import spaces

from typing import NewType, Tuple, Dict, List

EncodedObservation = NewType("EncodedObservation", np.ndarray)

class EncodedEmulator:
    def __init__(self, 
            start_string: str, 
            target_string: str, 
            max_steps: int, 
            max_string_len: int,
            all_chars: List[str] = chars,
            all_modes: List[str] = modes
            ):
        self._emulator: Emulator = Emulator(start_string, target_string, max_steps, max_string_len)
        self._action_encoder: Encoder = ActionEncoder(all_chars)
        self._char_encoder: Encoder = Encoder(all_chars)
        self._mode_encoder: Encoder = Encoder(all_modes)
        self._max_string_len: int = max_string_len

    def step(self, encoded_action) -> Tuple[EncodedObservation, int, bool, Dict]:
        #print("trying")
        #print(encoded_action)
        #print("-->|" + self._action_encoder.decode(encoded_action) + "|")
        ob, reward, done, info = self._emulator.step(
                self._action_encoder.decode(encoded_action))

        return self.__encode_ob(ob), reward, done, info

    def reset(self) -> EncodedObservation:
        self._emulator.reset()
        return self.__cur_encoded_ob()

    def render(self):
        self._emulator.render()

    def close(self):
        self._emulator.close()

    def __cur_encoded_ob(self) -> EncodedObservation:
        return self.__encode_ob(self._emulator.cur_observation())

    def __encode_ob(self, ob: EmulatorState) -> EncodedObservation:
        return np.concatenate([
                self._char_encoder.encode(ob.last_action),
                self._mode_encoder.encode(ob.mode),
                [1] if ob.blocking else [0],
                ob.curpos,
                self.__encode_string(ob.string)
        ]).astype(np.uint8)

    def __encode_string(self, s: ScreenString) -> np.ndarray:
        arrs = []
        for c in s.ljust(self._max_string_len):
            arrs.append(self._char_encoder.encode(c))
        return np.concatenate(arrs)

    def action_space(self):
        return spaces.Discrete(self._action_encoder.size())

    def observation_space(self):
        return spaces.Box(
                low=0, 
                high=5, 
                shape=(self.__cur_encoded_ob().size, ),
                dtype=np.uint8
                )

