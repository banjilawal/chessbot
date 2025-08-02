from typing import List

from assurance.result import Result, OperationStatus
from assurance.transaction_report import TransactionReport, StatusCode
from assurance.validation.validation_report import TestOutcome
from chess.geometry.coordinate.coordinate import Coordinate, Delta
from chess.piece.piece import ChessPiece
from chess.square.model.square import Square
from chess.square.repo.iterator import SquareIterator
from chess.geometry.coordinate.coordinate_validator import CoordinateValidator


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


    def square(self, coordinate: Coordinate) -> TransactionReport[Square]:
        method_name = "SquareRepo.find_square"

        validation_result = CoordinateValidator.coordinate_exists(coordinate)
        if validation_result.test_outcome is TestOutcome.FAILED_VALIDATION_TEST:
            return TransactionReport(
                method_name= method_name,
                status_code=StatusCode.FAILURE,
                operation_result= Result(status=OperationStatus.FAILURE, validation_result=validation_result)
            )
        square = self._squares[coordinate.row][coordinate.column]

        if square is None:
            return TransactionReport(
                method_name= method_name,
                status_code=StatusCode.SUCCESS,
                operation_result= Result.ok(f"No square at {coordinate} was found")
            )

        return TransactionReport(
            method_name= method_name, status_code=StatusCode.SUCCESS, operation_result= Result.ok(square)
        )


    def chess_piece(self, coordinate) -> TransactionReport[ChessPiece]:
        method_name = "SquareRepo.find_ches_piece"

        search_transaction_result = self.find_square(coordinate)
        if search_transaction_result.operation_result.payload is None:
            return TransactionReport(
                method_name,
                StatusCode.SUCCESS,
                Result.ok(f"There is no square at {coordinate} so ChessPiece at the location")
            )

        square = search_transaction_result.operation_result.payload
        if square.occupant is None:
            return TransactionReport(
                method_name,
                StatusCode.SUCCESS,
                Result.ok(f"There is no square at {coordinate} so ChessPiece at the location")
            )

        return TransactionReport(method_name, StatusCode.SUCCESS, Result.ok(square.occupant))


    def __str__(self) -> str:
        string = ""
        for row_index in reversed(range(len(self._grid))):  # start from top row (8) to bottom (1)
            row_squares = self._squares[row_index]
            row_str = " ".join(f"[{square.name}]" for square in row_squares)
            string += row_str + "\n"
        return string.strip()




