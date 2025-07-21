from abc import abstractmethod, ABC
from dataclasses import field, dataclass


@dataclass
class Rank(ABC):
    movement_strategy: 'MovementStrategy' = field(init=False, repr=False)

    def __post_init__(self):
        # Ensure subclass has set movement_strategy
        if not hasattr(self, 'movement_strategy') or self.movement_strategy is None:
            raise TypeError(f"{self.__class__.__name__} must initialize movement_strategy")

class PawnRank(Rank):
    def __init__(self, movement_strategy: 'PawnMovement'):
        self._movement_strategy = movement_strategy

    @property
    def movement_strategy(self) -> 'PawnMovement':
        return self._movement_strategy


class KnightRank(Rank):
    def __init__(self, movement_strategy: 'KnightMovement'):
        self._movement_strategy = movement_strategy

    @property
    def movement_strategy(self) -> 'KnightMovement':
        return self._movement_strategy


class BishopRank(Rank):
    def __init__(self, movement_strategy: 'BishopMovement'):
        self._movement_strategy = movement_strategy

    @property
    def movement_strategy(self) -> 'BishopMovement':
        return self._movement_strategy


class CastleRank(Rank):
    def __init__(self, movement_strategy: 'CastleMovement'):
        self._movement_strategy = movement_strategy

    @property
    def movement_strategy(self) -> 'CastleMovement':
        return self._movement_strategy


class QueenRank(Rank):
    def __init__(self, movement_strategy: 'QueenMovement'):
        self._movement_strategy = movement_strategy

    @property
    def movement_strategy(self) -> 'QueenMovement':
        return self._movement_strategy


class KingRank(Rank):
    def __init__(self, movement_strategy: 'KingMovement'):
        self._movement_strategy = movement_strategy

    @property
    def movement_strategy(self) -> 'KingMovement':
        return self._movement_strategy
