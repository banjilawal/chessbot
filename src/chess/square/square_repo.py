from typing import List, Optional

from assurance.result import Result
from assurance.transaction_result import TransactionResult
from chess.geometry.board.coordinate import Coordinate
from chess.square.model.square import Square
from chess.validator.coordinate_validator import CoordinateValidator


class SquareRepo:
    data: List[List[Square]]

    def __init__(self, squares: List[List[Square]]):
        self.data = squares

    def find_square(self, coordinate: Coordinate) -> TransactionResult:
        validation_result = CoordinateValidator.validate(coordinate)
        if validation_result.is_failure:
            return Result("SquareRepo.find_square", validation_result)
            return TransactionResult("SquareRepo.find_square", validation_result)

a