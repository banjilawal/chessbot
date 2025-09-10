class XAboveBoundsException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a null-pkg's x value is
    larger than KNIGHT SIZE raise this exception
    """

    ERROR_CODE = "VECTOR_X_DIMENSION_ABOVE_MAX_STEP_SIZE"
    DEFAULT_MESSAGE = f"Vector.x > {KNIGHT_STEP_SIZE}. An exception has been raiser"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"