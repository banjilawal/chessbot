# src/logic/square/database/core/util/occupation/token/exception/super.py

"""
Module: logic.square.database.core.util.occupation.token.exception.super
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

___all__ = [
    # ======================# OCCUPATION_SERVICE EXCEPTION #======================#
    "OccupationServiceException",
]


from logic.system import ServiceException


# ======================# OCCUPATION_SERVICE EXCEPTION #======================#
class OccupationServiceException(ServiceException):
    """
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a failure occurred in OccupationService.
    2.  The method where the error occurred is identified in the exception nested directly underneath.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "OCCUPATION_SERVICE_EXCEPTION"
    MSG = "OccupationService raised an exception."