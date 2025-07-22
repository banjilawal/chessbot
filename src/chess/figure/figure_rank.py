from abc import abstractmethod, ABC


class FigureRank(ABC):
    _movement_strategy: MovementStrategy
    def __init__(self, movement_strategy: MovementStrategy):
        if movement_strategy is None:
            raise TypeError("movement_strategy cannot be None")
        self._movement_strategy = movement_strategy

    @property
    def movement_strategy(self) -> MovementStrategy:
        return self._movement_strategy


class PawnRank(FigureRank):
    def __init__(self, movement_strategy: 'PawnMovement'):
        super().__init__(movement_strategy)


class KnightRank(FigureRank):
    def __init__(self, movement_strategy: 'KnightMovement'):
        super().__init__(movement_strategy)


class BishopRank(FigureRank):
    def __init__(self, movement_strategy: 'BishopMovement'):
        super().__init__(movement_strategy)


class CastleRank(FigureRank):
    def __init__(self, movement_strategy: 'CastleMovement'):
        super().__init__(self, movement_strategy)


class KingRank(FigureRank):
    def __init__(self, movement_strategy: 'KingMovement'):
        super().__init__(movement_strategy)


class QueenRank(FigureRank):
    def __init__(self, movement_strategy: 'QueenMovement'):
        super().__init__(self, movement_strategy)


