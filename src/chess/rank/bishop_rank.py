
from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.rank.rank import Rank
from chess.motion.logic.diagonal_pattern import DiagonalPattern


class BishopRank(Rank):
    def __init__(self, movement_strategy: 'BishopSearchPattern'):
        super().__init__(movement_strategy)
