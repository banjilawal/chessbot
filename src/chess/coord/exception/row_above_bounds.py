class RowAboveBoundsException(CoordException):
    """
    If a row >= ROW_SIZE RowAboveBoundsException is raised.
    """

    ERROR_CODE = "ROW_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coord.row > {ROW_SIZE-1}. This outside the dimension of the board"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"