# src/chess/square/database/core/util/occupation/token/exception/catchall.py

"""
Module: chess.square.database.core.util.occupation.token.exception.catchall
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

___all__ = [
    # ======================# OCCUPATION_SERVICE EXCEPTION #======================#
    "OccupationServiceException",
]


from chess.system import ServiceException


# ======================# OCCUPATION_SERVICE EXCEPTION #======================#
class OccupationServiceException(ServiceException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by OccupationService methods that return Result objects.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "OCCUPATION_SERVICE_ERROR"
    DEFAULT_MESSAGE = "OccupationService raised an exception."