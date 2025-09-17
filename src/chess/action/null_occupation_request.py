from chess.exception import NullException


class NullRequestException(NullException):
    """
    Raised if a action is null. Each Action class will have a corresponding NullException. Best practice
    is raise one of NUllRequest subclasses when possible.
    """

    ERROR_CODE = "NULL_REQUEST_ERROR"
    DEFAULT_MESSAGE = f"Action cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NullOccupationRequestException(NullRequestException):
    """
    Raised if an OOccupationDirective is null.
    """

    ERROR_CODE = "NULL_OCCUPATION_REQUEST_ERROR"
    DEFAULT_MESSAGE = f"OOccupationDirective cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NullOPromotionRequestException(NullRequestException):
    """
    Raised if an Promote is null.
    """

    ERROR_CODE = "NULL_PROMOTION_REQUEST_ERROR"
    DEFAULT_MESSAGE = f"Promote cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
