from chess.exception.offset.base import CoordinateOffsetException


class ScalarBelowLowerBoundException(CoordinateOffsetException):
    ERROR_CODE = "NEGATIVE_OFFSET_MULTIPLICATION_FACTOR_ERROR"
    DEFAULT_MESSAGE = f"Offset multiplication factor cannot be negative."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ZeroScalarException(CoordinateOffsetException):
    ERROR_CODE = "MULTIPLY_OFFSET_BY_ZERO_ERROR"
    DEFAULT_MESSAGE = f"Offset multiplication factor cannot be zero."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ScalarAboveUpperBoundException(CoordinateOffsetException):
    ERROR_CODE = "OFFSET_FACTOR_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = (
        f"Offset multiplication factor is outside "
        f"the chessboard range of 1 to 7 inclusive."
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class RowDeltaOverflowExceptioDn(CoordinateOffsetException):
    ERROR_CODE = "ROW_DELTA_MULTIPLICATION_OVERFLOW_ERROR"
    DEFAULT_MESSAGE = f"Offset.delta_row multiplication result outside board dimension"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class ColumnDeltaOverflowExceptioDn(CoordinateOffsetException):
    ERROR_CODE = "ROW_DELTA_MULTIPLICATION_OVERFLOW_ERROR"
    DEFAULT_MESSAGE = f"Offset.delta_row multiplication result outside board dimension"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class OffsetMultiplicationOverflowException(CoordinateOffsetException):
    ERROR_CODE = "OFFSET_MULTIPLICATION_ERROR"
    DEFAULT_MESSAGE = f"Offset scalar multiplication result outside board dimension"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"