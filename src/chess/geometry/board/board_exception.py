from chess.system_config import ROW_SIZE, COLUMN_SIZE

class MissingBoardException(ChessException):
    default_message = "ChessBoard cannot be None."

class MissingGridException(ChessException):
    default_message = "The ChessBoard has no grid of squares."

class ColumnIndexOutOfBoundsException(ChessException):
    default_message = "Column index out of bounds."

class RowIndexOutOfBoundsException(ChessException):
    default_message = "Row index out of bounds."

class ArrayDimensionException(ChessException):
    default_message = f"Grid violates the {ROW_SIZE}x{COLUMN_SIZE} board requirement"
