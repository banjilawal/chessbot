from chess.exception.base import ChessException

"""
Thrown if square does not contain a friendly and Event.MARK_OBSTRUCTION event was in the outcome 
"""
class InconsistentMarkObstructionException(ChessException):
    """
    Thrown if square does not contain a friendly and Event.MARK_OBSTRUCTION event was in the outcome
    """
    ERROR_CODE = "MARK_OBSTRUCTION_EVENT_ERROR"
    DEFAULT_MESSAGE = (
        "The square does not contain a friendly. Granting MARK_OBSTRUCTION was an error"
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