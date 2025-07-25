from abc import ABC

from chess.motion.movement import MovementStrategy


class Rank(ABC):
    _movement_strategy: MovementStrategy
    def __init__(self, movement_strategy: MovementStrategy):
        if movement_strategy is None:
            raise TypeError("movement_strategy cannot be None")
        self._movement_strategy = movement_strategy

    @property
    def movement_strategy(self) -> MovementStrategy:
        return self._movement_strategy










    def












