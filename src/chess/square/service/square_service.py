from typing import List, Optional

from assurance.transaction_report import TransactionReport
from chess.geometry.coordinate.coordinate import Coordinate
from chess.team.model.piece import ChessPiece
from chess.square.model.square import Square
from chess.square.repo.square_repo import SquareRepo


class SquareService:
    _square_repo: SquareRepo

    def __init__(self, square_repo: SquareRepo):
        self.square_repo = square_repo


    def squares(self) -> List[List[Square]]:
        return self._square_repo.squares


    def empty_squares(self) -> List[Square]:
        matches: List[Square] = []
        iterator = self._square_repo.iterator()
        for square in self._square_repo.iterator():
            if square.occupant is None:
                matches.append(square)
        return matches


    def occupied_squares(self) -> List[Square]:
        matches: List[Square] = []
        iterator = self._square_repo.iterator()
        for square in self._square_repo.iterator():
            if square.occupant is not None:
                matches.append(square)
        return matches

    def find_square(self, coordinate: Coordinate) -> Optional[Square]:
        return self._square_repo.find_square_by_coordinate(coordinate)


    def find_square_by_name(self, name: str) -> Optional[Square]:


    def capture_square(self, chess_piece: ChessPiece, coordinate: Coordinate):



