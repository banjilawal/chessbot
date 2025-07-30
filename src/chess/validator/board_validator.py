from typing import List
from chess.geometry.square import Square
from chess.geometry.coordinate import Coordinate
from chess.system_config import ROW_SIZE, COLUMN_SIZE


class BoardValidator:

    @staticmethod
    def validate(board: 'ChessBoard') -> bool:

        if board is None:
            raise ValueError("ChessBoard cannot be None.")

        grid = getattr(board, 'grid', None)
        if grid is None:
            raise ValueError("ChessBoard has no grid attribute.")

        if len(grid) != ROW_SIZE:
            raise ValueError(f"ChessBoard must have 8 rows, found {len(grid)}.")

        for row_index, row in enumerate(grid):
            if not isinstance(row, list):
                raise ValueError(f"Row {row_index} is not a list.")

            if len(row) != COLUMN_SIZE:
                raise ValueError(f"Row {row_index} must have 8 columns, found {len(row)}.")

            for column_index, square in enumerate(row):
                if not isinstance(square, Square):
                    raise ValueError(f"Element at row {row_index}, col {column_index} is not a Square.")

        return True
