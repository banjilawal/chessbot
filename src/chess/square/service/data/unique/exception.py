from chess.system import UniqueDataServiceException

__all__ = [
    "UniqueDataServiceException",
    "AddingDuplicateSquareException",
]


class UniqueSquareDataServiceException(UniqueDataServiceException):
    """
    Super class of exceptions raised by UniqueSquareDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "UNIQUE_SQUARE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueSquareDataService raised an exception."


class AddingDuplicateSquareException(UniqueSquareDataServiceException):
    """Raised when trying to add a duplicate Square to a list of Squares."""
    ERROR_CODE = "DUPLICATE_SQUARE_ADDITION_ERROR"
    DEFAULT_MESSAGE = "SquareDataService cannot add duplicate Squares to the list."