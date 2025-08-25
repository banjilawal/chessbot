class ChessException(Exception):

    DEFAULT_MESSAGE = "Chess error occurred"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
