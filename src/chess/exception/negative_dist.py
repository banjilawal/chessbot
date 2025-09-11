from chess.exception.coord_exception import CoordException


class NegativeDistanceMetric(CoordException):
    ERROR_CODE = "NEGATIVE_DISTANCE_METRIC_ERROR"
    DEFAULT_MESSAGE = f"Unexpected negative distance metric error"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



