from chess.exception.coordinate_stack.coord_stack import CoordinateStackException


class CurrentCoordinateInconsistentStateException(CoordinateStackException):
    ERROR_CODE = "CURRENT_COORDINATE_STATE_ERROR"
    DEFAULT_MESSAGE = "CoordinateStack's current coordinate is in an inconsistent state"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"