class NumberOfBoardSquaresOutOfBoundsException(BoardException):
    """Raised if the Board does not contain 64 Squares. This should never happen."""
    ERROR_CODE = "NUMBER_OF_BOARD_SQUARES_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The number of Square instance in Board is out of bounds. Only 64 Squares are allowed."