class ChessException(Exception):
    """Base exception with default message support"""
    default_message = "Chess arena error occurred"

    def __init__(self, message=None, **kwargs):
        self.message = message or self.default_message
        self.context = kwargs  # Store any additional context
        super().__init__(self.message)

    def __str__(self):
        if self.context:
            return f"{self.message} [Context: {self.context}]"
        return self.message

class NegativeIdException(ChessException):
    """Exception raised when an id is negative"""
    default_message = "Id cannot be negative"

class MissingIdException(ChessException):
    """Exception raised when an id is negative"""
    default_message = "The id is missing. Passing null id not allowed."

class MissingNameException(ChessException):
    """Exception raised when an id is negative"""
    default_message = "The name is missing. Passing null name not allowed."