from typing import List

from assurance.result import Result, ResultStatus
from assurance.transaction_result import TransactionResult, StatusCode
from assurance.validation.validatin_report import TestOutcome
from chess.geometry.board.coordinate import Coordinate, Delta
from chess.piece.piece import ChessPiece
from chess.square.model.square import Square
from chess.square.repo.iterator import SquareIterator
from assurance.validation.coordinate_validator import CoordinateValidator


class SquareRepo:
    _squares: List[List[Square]]


    def __init__(self, squares: List[List[Square]]):
        self._squares = squares


    @property
    def squares(self) -> List[List[Square]]:
        return self._squares


    def iterator(
        self,
        index: Coordinate = Coordinate(0, 0),
        delta: Delta=Delta(delta_column=1, delta_row=1)
     ) -> SquareIterator:
        return SquareIterator(self._squares, index, delta)


    def square(self, coordinate: Coordinate) -> TransactionResult[Square]:
        method_name = "SquareRepo.find_square"

        validation_result = CoordinateValidator.coordinate_exists(coordinate)
        if validation_result.test_outcome is TestOutcome.FAILED_VALIDATION_TEST:
            return TransactionResult(
                transaction_method_name = method_name,
                status_code=StatusCode.FAILURE,
                outcome= Result(status=ResultStatus.FAILURE, validation_result=validation_result)
            )
        square = self._squares[coordinate.row][coordinate.column]

        if square is None:
            return TransactionResult(
                transaction_method_name = method_name,
                status_code=StatusCode.SUCCESS,
                outcome= Result.ok(f"No square at {coordinate} was found")
            )

        return TransactionResult(
            transaction_method_name = method_name, status_code=StatusCode.SUCCESS, outcome= Result.ok(square)
        )


    def chess_piece(self, coordinate) -> TransactionResult[ChessPiece]:
        method_name = "SquareRepo.find_ches_piece"

        search_transaction_result = self.find_square(coordinate)
        if search_transaction_result.outcome.payload is None:
            return TransactionResult(
                method_name,
                StatusCode.SUCCESS,
                Result.ok(f"There is no square at {coordinate} so ChessPiece at the location")
            )

        square = search_transaction_result.outcome.payload
        if square.occupant is None:
            return TransactionResult(
                method_name,
                StatusCode.SUCCESS,
                Result.ok(f"There is no square at {coordinate} so ChessPiece at the location")
            )

        return TransactionResult(method_name, StatusCode.SUCCESS, Result.ok(square.occupant))




