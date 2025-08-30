from chess.exception.base import ChessException


class MarkObstructionPermissionInconsistencyException(ChessException):
    ERROR_CODE = "MARK_OBSTRUCTION_PERMISSION_ERROR"
    DEFAULT_MESSAGE = (
        "The square does not contain a friendly. Granting MARK_OBSTRUCTION was an error"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



class AttackPermissionInconsistencyException(ChessException):
    ERROR_CODE = "ATTACK_PERMISSION_ERROR"
    DEFAULT_MESSAGE = (
        "The square does not contain an enemy. Granting ATTACK_PERMISSION was an error"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"