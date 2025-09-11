from chess.exception.chess_exception import ChessException

"""
Super class for Piece exceptions
"""
class CommanderException(ChessException):
    """
    Super class for exceptions raised by Piece objects
    """

    ERROR_CODE = "COMMANDER_ERROR"
    DEFAULT_MESSAGE = "Commander raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



class SideRecordException(ChessException):
    """
    Super class for exceptions raised by Piece objects
    """

    ERROR_CODE = "COMMANDER_ERROR"
    DEFAULT_MESSAGE = "Commander raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"