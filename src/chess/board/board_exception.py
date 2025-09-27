from chess.exception import NullException


class BoardException(ChessException):
    ERROR_CODE = "BOARD_ERROR"
    DEFAULT_MESSAGE = "Board raised an team_exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class IncompleteBoardTransactionException(ChessException):
    ERROR_CODE = "BOARD_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "The board is an inconsistent state. Transasaction failed."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class RemovePieceFromBoardException(ChessException):
    ERROR_CODE = "REMOVE_FROM_BOARD_ERROR"
    DEFAULT_MESSAGE = "Removing captured discovery from the board failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class NullBoardException(NullException):
    """
    If null is passed as a parameter instead of a Board then NullBoardException is raised
    """

    ERROR_CODE = "NULL_BOARD_ERROR"
    DEFAULT_MESSAGE = "Board cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class IncompleteBoardTransactionException(ChessException):
    ERROR_CODE = "BOARD_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "The board is an inconsistent state. Transasaction failed."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class FailedPieceRemovalException(ChessException):
    ERROR_CODE = "REMOVE_FROM_BOARD_ERROR"
    DEFAULT_MESSAGE = "Removing captured discovery from the board failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"














