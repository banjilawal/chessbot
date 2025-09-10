from chess.exception.chess_exception import ChessException

"""
Thrown if square does not contain a friendly and Event.RECORD_ENCOUNTER event was in the outcome 
"""
class CorruptRecordEventException(ChessException):
    """
    Thrown if square does not contain a friendly and Event.RECORD_ENCOUNTER event was in the outcome
    """
    ERROR_CODE = "MARK_OBSTRUCTION_EVENT_ERROR"
    DEFAULT_MESSAGE = (
        "The square does not contain a friendly. Granting RECORD_ENCOUNTER was an error"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Thrown if square does not contain a and enemy and Event.ATTACK was iin the outcome 
"""
class AttackPermissionInconsistencyException(ChessException):
    """
    Thrown if square does not contain a and enemy and Event.ATTACK was iin the outcome
    """
    ERROR_CODE = "ATTACK_PERMISSION_ERROR"
    DEFAULT_MESSAGE = (
        "The square does not contain an enemy. Granting ATTACK_PERMISSION was an error"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"