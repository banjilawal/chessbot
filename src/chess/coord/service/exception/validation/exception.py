
from chess.coord import CoordServiceException
from chess.system import NullException, ValidationException


__all__ = [
    "InvalidCoordServiceException",
    "NullException",
]

# ====================== COORD_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidCoordServiceException(CoordServiceException, ValidationException):
    """Catchall Exception for CoordSERVICEValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "COORD_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CoordService validation failed."


# ====================== NULL COORD EXCEPTIONS #======================#
class NullCoordServiceException(CoordServiceException, NullException):
    """Raised if an entity, method, or operation requires Coord but gets validation instead."""
    ERROR_CODE = "NULL_COORD_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordService cannot be validation."


