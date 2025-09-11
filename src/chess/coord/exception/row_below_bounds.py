class RowBelowBoundsException(CoordException):
    """
    If row < 0 RowBelowBoundsException is raised. Domain specific alternative
    to ArrayIndexOutOfBoundsException
    """

    ERROR_CODE = "ROW_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coord.row < 0. This outside the dimension of the board"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"