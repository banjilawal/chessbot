
from abc import ABC, abstractmethod
from typing import Dict

from chess.board.chess_board import ChessBoard
from chess.common.geometry import Coordinate
from chess.figure.chess_piece import ChessPiece
from chess.motion.motions.diagonal import Motion


class MovementStrategy(ABC):
    _move_rules: {}
    """ A MovementStrategy is a collection of MoveRules that define how a piece can move."""

    def __init__(self, rules: list[Motion]):
        self._move_rules = {}
        for rule in rules:
            class_name = type(rule).__name__
            if class_name not in self._move_rules:
                self._move_rules[class_name] = rule

    def check_basic_conditions(self, chess_piece: ChessPiece, board: 'Board', destination: 'Coordinate') -> bool:
        if chess_piece is None:
            print("[Warning] Mover cannot be None. It cannot move.")
            return False
        if board is None:
            print("[Warning] Board cannot be None. Cannot move.")
            return False
        if chess_piece.coordinate is None:
            print("[Warning] chess_piece has not coordinate. Cannot move.")
            return False
        if destination is None:
            print("[Warning] Destination coordinate cannot be None. Cannot move.")
            return False
        return True

    @abstractmethod
    def possible_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        """Return a list of valid destinations from the given origin."""
        pass


    @property
    def move_rules(self) -> Dict[str, Motion]:
        return self._move_rules.copy()


