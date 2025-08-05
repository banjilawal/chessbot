from typing import List, Optional

from chess.geometry.coordinate.coordinate import Coordinate
from chess.square.model.square import Square
from chess.square.repo.square_repo import SquareRepo


class SquareService:
    _repo: SquareRepo

    def __init__(self, repo: SquareRepo):
        self._repo = repo


    def squares(self) -> List[List[Square]]:
        return self._repo.squares


    def empty_squares(self) -> List[Square]:
        return self._repo.empty_squares()


    def occupied_squares(self) -> List[Square]:
        return self._repo.occupied_squares()

    def find_square(self, coordinate: Coordinate) -> Optional[Square]:
        return self._repo.find_square_by_coordinate(coordinate)


    def find_square_by_id(self, square_id) -> Optional[Square]:
        return self._repo.find_square_by_id(square_id)


    def find_square_by_name(self, name:str) -> Optional[Square]:
        return self._repo.find_square_by_name(name)



