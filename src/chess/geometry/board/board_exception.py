from chess.common.exceptions import ChessException
from chess.common.config import ROW_SIZE, COLUMN_SIZE

class BoardException(ChessException):
    default_message = "An error occurred in the ChessBoard."

class CoordinateException(BoardException):
    default_message = "An error occurred in the Coordinate."

class MissingBoardException(BoardException):
    default_message = "ChessBoard does not exist.Passing null board not allowed."

class MissingGridException(BoardException):
    default_message = "The ChessBoard has no grid of squares. Passing null grid not allowed."

class ArrayDimensionException(BoardException):
    default_message = f"Grid violates the {ROW_SIZE}x{COLUMN_SIZE} board requirement"

class MissingCoordinateException(CoordinateException):
    default_message = "Coordinate does not exist. Passing null coordinate not allowed"

class CoordinateRowOutOfBoundsException(CoordinateException):
    default_message = f"Coordinate row out of bounds."

class CoordinateColumnIndexOutOfBoundsException(CoordinateException):
    default_message = "Coordinate column out of bounds."
