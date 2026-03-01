# src/logic/square/database/core/util/occupation/token/exception/exist.py

"""
Module: logic.square.database.core.util.occupation.token.exception.exist
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""



__all__ = [
    # ======================# VISIT_DESTINATION_NOT_FOUND EXCEPTION #======================#
    "VisitDestinationNotFoundException",
]

from logic.square import SquareDebugException


# ======================# VISIT_DESTINATION_NOT_FOUND EXCEPTION #======================#
class VisitDestinationNotFoundException(SquareDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing  UpdateResult was returned because a token wanted to occupy a square which does not exist in
        the SquareStack.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VISIT_DESTINATION_NOT_FOUND_EXCEPTION"
    MSG = "SquareVisit start failed: token wanted to visit square which does not exist."