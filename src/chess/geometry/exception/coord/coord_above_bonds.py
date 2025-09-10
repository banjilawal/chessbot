class ColumnAboveBoundsException(CoordException):
    """
    If Coord.column > DIMENSION ColumnAboveBoundsException is raised.
    """

    ERROR_CODE = "COLUMN_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coord.column > {COLUMN_SIZE-1}. This outside the dimension of the board"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"