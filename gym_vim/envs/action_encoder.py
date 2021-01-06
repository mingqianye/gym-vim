import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from typing import Tuple, List, Dict, TypeVar, Generic

T = TypeVar("T")

class ActionEncoder(Generic[T]):
    def __init__(self, ll: List[T]): 
        self.d1: Dict[T, int] = {}
        self.d2: Dict[int, T] = {}

        for i, elem in enumerate(ll):
            self.d1[elem] = i
            self.d2[i] = elem

    def encode(self, item: T) -> int:
        return self.d1[item]

    def decode(self, num: int) -> T:
        return self.d2[num]

    def get_dict(self) -> Dict[T, int]:
        return self.d1

    def size(self) -> int:
        return len(self.d1)
