import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from typing import Tuple, List, Dict, TypeVar, Generic

T = TypeVar("T")

class Encoder(Generic[T]):
    label_encoder: LabelEncoder
    lookup_dict: Dict[str, np.ndarray] = {}

    def __init__(self, ll: List[T]): 
        arr0 = Encoder.convert_to_string_arr(ll)

        arr1 = np.array(arr0)

        self.label_encoder = LabelEncoder()
        integer_encoded = self.label_encoder.fit_transform(arr1)

        arr2 = integer_encoded.reshape(len(integer_encoded), 1)

        onehot_arr = OneHotEncoder(sparse=False) \
            .fit_transform(arr2)

        for i, item in enumerate(arr0):
            self.lookup_dict[item] = onehot_arr[i]

    def encode(self, item: T) -> np.ndarray:
        return self.lookup_dict[str(item)]

    def decode(self, arr: np.ndarray) -> np.ndarray:
        return self.label_encoder.inverse_transform([np.argmax(arr)])

    def size(self) -> int:
        return len(self.lookup_dict)

    def convert_to_string_arr(ll: List[T]) -> List[str]:
        ss = []
        for l in ll:
            ss.append(str(l))
        return ss

def encode(ss: List[str]):
    arr = np.array(ss)
    integer_encoded = LabelEncoder().fit_transform(arr)

    onehot_encoded = OneHotEncoder(sparse=False).fit_transform(
            integer_encoded.reshape(len(integer_encoded), 1)
    )
    return onehot_encoded
