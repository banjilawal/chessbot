from typing import Optional

from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate

from chess.transaction.transaction_result import TransactionResult, Failure, StatusCode

class CoordinateValidator:

    @staticmethod
    def validate_coordinate_on_board(coordinate: Optional[Coordinate], board: Optional[Board]) -> TransactionResult:
        method = "CoordinateValidator.validate_coordinate_on_board"

        if board is None:
            return TransactionResult(
                method_name=method,
                status=StatusCode.FAILURE,
                outcome=Failure(StatusCode.FAILURE, "Board cannot be None.")
            )

        if coordinate is None:
            return TransactionResult(
                method_name=method,
                status=StatusCode.FAILURE,
                outcome=Failure(StatusCode.FAILURE, "Coordinate cannot be None.")
            )

        rows = len(board.grid)
        columns = len(board.grid[0]) if rows > 0 else 0

        if coordinate.row < 0 or coordinate.row >= rows:
            return TransactionResult(
                method_name=method,
                status=StatusCode.FAILURE,
                outcome=Failure(StatusCode.FAILURE, f"Row {coordinate.row} is out of board bounds (0-{rows - 1}).")
            )

        if coordinate.column < 0 or coordinate.column >= columns:
            return TransactionResult(
                method_name=method,
                status=StatusCode.FAILURE,
                outcome=Failure(StatusCode.FAILURE, f"Column {coordinate.column} is out of board bounds (0-{columns - 1}).")
            )

        return TransactionResult(method_name=method, status=StatusCode.SUCCESS, outcome=StatusCode.SUCCESS)
