

from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")
class JSONConverter(ABC, Generic[T]):
    
    @classmethod
    def convert_to_json(cls, obj: T):
        pass