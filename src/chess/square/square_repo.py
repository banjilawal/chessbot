from typing import List, Optional

from assurance.result import Result, ResultStatus
from assurance.transaction_result import TransactionResult, StatusCode
from assurance.validation_result import ValidationStatus
from chess.geometry.board.coordinate import Coordinate
from chess.piece.piece import ChessPiece
from chess.square.model.square import Square
from chess.validator.coordinate_validator import CoordinateValidator


class SquareRepo:
    _squares: List[List[Square]]

    def __init__(self, squares: List[List[Square]]):
        self._squares = squares

    @property
    def squares(self) -> List[List[Square]]:
        return self._squares


    def find_square(self, coordinate: Coordinate) -> TransactionResult[Square]:
        method_name = "SquareRepo.find_square"

        validation_result = CoordinateValidator.coordinate_exists(coordinate)
        if validation_result.status is ValidationStatus.INVALID:
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


    def find_ches_piece(self, coordinate) -> TransactionResult[ChessPiece]:
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


