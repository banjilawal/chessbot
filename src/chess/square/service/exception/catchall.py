# src/chess/square/service/exception/catchall.py

"""
Module: chess.square.service.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""


from chess.system import ServiceException

__all__ = [
    # ======================# SQUARE_SERVICE EXCEPTION #======================#
    "SquareServiceException",
]


# ======================# SQUARE_SERVICE EXCEPTION #======================#
class SquareServiceException(ServiceException):
    """
    # ROLE: Catchall, Exception Messaging

    # RESPONSIBILITIES:
    1.  Outermost layer of the 3-part exception chain that is created when a SquareService operation fails.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareService raised an exception."