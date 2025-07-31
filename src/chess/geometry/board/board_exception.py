from chess.system_config import ROW_SIZE, COLUMN_SIZE

class MissingBoardException(ChessException):
    default_message = "ChessBoard does not exist.Passing null board not allowed."

class MissingGridException(ChessException):
    default_message = "The ChessBoard has no grid of squares. Passing null grid not allowed."

class ArrayDimensionException(ChessException):
    default_message = f"Grid violates the {ROW_SIZE}x{COLUMN_SIZE} board requirement"

class MissingCoordinateException(ChessException):
    default_message = "Coordinate does not exist. Passing null coordinate not allowed"

class CoordinateRowOutOfBoundsException(ChessException):
    default_message = f"Coordinate row out of bounds."

class CoordinateColumnIndexOutOfBoundsException(ChessException):
    default_message = "Coordinate column out of bounds."
