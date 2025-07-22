import string
from abc import ABC, abstractmethod
from typing import Dict

from chess.common.geometry import Coordinate
from chess.figure.chess_piece import ChessPiece
from chess.motion.diagonal import Move


class MovementStrategy(ABC):
    _move_rules: Dict[string, Move]
    """ A MovementStrategy is a collection of MoveRules that define how a piece can move."""

    def __init__(self, rules: list[Move]):
        self._move_rules = [string, Move]
        for rule in rules:
            class_name = rule.__name__
            if class_name not in self._move_rules:
                self._move_rules[rule.__name__] = rule

    @abstractmethod
    def destinations(self, origin: Coordinate) -> list[Coordinate]:
        """Return a list of valid destinations from the given origin."""
        pass

    @abstractmethod
    def best_destinations(self, origin: Coordinate) -> list[Coordinate]:
        """Return the best destination from the given origin."""
        pass

    @abstractmethod
    def worst_destinations(self, origin: Coordinate) -> list[Coordinate]:
        """Return the worst destination from the given origin."""
        pass

    @abstractmethod
    def is_valid_move(self, origin: Coordinate, destination: Coordinate) -> bool:
        """Return True if the given move is valid, False otherwise."""
        pass

    @property
    def move_rules(self) -> Dict[string, Move]:
        return list(self._move_rules)

    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination: Coordinate) -> bool:
        """Perform the move if valid. Return True if successful, False otherwise."""
        pass

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
