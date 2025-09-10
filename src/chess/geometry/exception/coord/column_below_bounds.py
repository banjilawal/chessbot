class ColumnBelowBoundsException(CoordException):
    """
    If Coord.column < 0 ColumnBelowBoundsException is raised.
    """

    ERROR_CODE = "COLUMN_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coordinate.column < 0. This outside the dimension of the board"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"