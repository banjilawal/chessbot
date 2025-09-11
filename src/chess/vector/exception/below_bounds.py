class VectorBelowBoundsException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a null-pkg's x value is
    larger than KNIGHT SIZE raise this exception
    """

    ERROR_CODE = "VECTOR_BELOW_BOUNDS_EXCEPTION"
    DEFAULT_MESSAGE = f"Vector is below bounds"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"