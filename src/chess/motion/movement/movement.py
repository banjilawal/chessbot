
from abc import ABC, abstractmethod
from typing import Dict, Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.piece.piece import Piece
from chess.motion.definition.diagonal import Definition
from chess.team.home import TeamHome


class MovementStrategy(ABC):
    _move_rules: {}
    """ A MovementStrategy is a collection of MoveRules that definition how a piece can move."""

    def __init__(self, rules: list[Definition]):
        self._move_rules = {}
        for rule in rules:
            class_name = type(rule).__name__
            if class_name not in self._move_rules:
                self._move_rules[class_name] = rule

    def check_basic_conditions(self, chess_piece: Piece, board: 'PodBoard', destination: 'Coordinate') -> bool:
        if chess_piece is None:
            print("[Warning] Mover cannot be None. It cannot move.")
            return False
        if board is None:
            print("[Warning] PodBoard cannot be None. Cannot move.")
            return False
        if chess_piece.coordinate is None:
            print("[Warning] chess_piece has not coordinate. Cannot move.")
            return False
        if destination is None:
            print("[Warning] Destination coordinate cannot be None. Cannot move.")
            return False
        return True

    @abstractmethod
    def possible_destinations(self, origin: Coordinate, board: Board, team_home: Optional[TeamHome] = None) -> list[Coordinate]:
        """Return a list of valid destinations from the given origin."""
        pass


    @property
    def move_rules(self) -> Dict[str, Definition]:
        return self._move_rules.copy()


