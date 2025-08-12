from chess.exception.negative_id_exception import ChessException
from chess.common.config import ROW_SIZE, COLUMN_SIZE

class BoardException(ChessException):
    default_message = "An error occurred in the ObsoleteChessBoard."

class CoordinateException(BoardException):
    default_message = "An error occurred in the Coordinate."

class MissingBoardException(BoardException):
    default_message = "ObsoleteChessBoard does not exist.Passing null chess_board not allowed."

class MissingGridException(BoardException):
    default_message = "The ObsoleteChessBoard has no board of squares. Passing null board not allowed."

class ArrayDimensionException(BoardException):
    default_message = f"Grid violates the {ROW_SIZE}x{COLUMN_SIZE} chess_board requirement"

class MissingCoordinateException(CoordinateException):
    default_message = "Coordinate does not exist. Passing null coordinate not allowed"

class CoordinateRowOutOfBoundsException(CoordinateException):
    default_message = f"Coordinate row out of bounds."

class CoordinateColumnIndexOutOfBoundsException(CoordinateException):
    default_message = "Coordinate column out of bounds."
