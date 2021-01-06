import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from typing import Tuple, List, Dict, TypeVar, Generic

T = TypeVar("T")

class Encoder(Generic[T]):
    def __init__(self, ll: List[T]): 
        ss = Encoder._convert_to_string_arr(ll)

        self._label_encoder, label_encoded = Encoder._label_encode(
            np.array(ss)
        )

        onehot_encoded = Encoder._onehot_encode(label_encoded)

        self._lookup_dict: Dict[str, np.ndarray] = {}

        for i, item in enumerate(ss):
            self._lookup_dict[item] = onehot_encoded[i]

    def encode(self, item: T) -> np.ndarray:
        return self._lookup_dict[str(item)]

    def decode(self, arr: np.ndarray) -> str:
        return self._label_encoder.inverse_transform([np.argmax(arr)])[0]

    def get_dict(self) -> Dict[str, np.ndarray]:
        return self._lookup_dict

    def size(self) -> int:
        return len(self._lookup_dict)

    def _label_encode(ss: List[str]) -> Tuple[LabelEncoder, np.ndarray]:
        label_encoder = LabelEncoder()
        return label_encoder, label_encoder.fit_transform(ss)

    def _onehot_encode(label_encoded: np.ndarray) -> np.ndarray:
        return OneHotEncoder(sparse=False).fit_transform(
            label_encoded.reshape(len(label_encoded), 1)
        )

    def _convert_to_string_arr(ll: List[T]) -> List[str]:
        ss = []
        for l in ll:
            ss.append(str(l))
        return ss
