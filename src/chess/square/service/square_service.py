from typing import List

from chess.square.model.square import Square
from chess.square.repo.square_repo import SquareRepo


class SquareService:
    _square_repo: SquareRepo

    def __init__(self, square_repo: SquareRepo):
        self.square_repo = square_repo


    def empty_squares(self) -> List[Square]:
        matches: List[Square] = []

        for square in self._square_repo.squares:
            if square. is None and square not in matches:
                matches.append(square)

