from abc import ABC

from chess.motion.search import SearchPattern


class Rank(ABC):
    _movement_strategy: SearchPattern
    def __init__(self, movement_strategy: SearchPattern):
        if movement_strategy is None:
            raise TypeError("movement_strategy cannot be None")
        self._movement_strategy = movement_strategy

    @property
    def movement_strategy(self) -> SearchPattern:
        return self._movement_strategy










    def












