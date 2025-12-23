from abc import ABC
from typing import TypeVar

from chess.system import Finder

T = TypeVar("T")

class Lookup(ABC, Finder[T]):
    pass