# src/chess/square/service/visitation/exception/start/add.py

"""
Module: chess.square.service.visitation.exception.start.add
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

__all__ = [
    # ======================# STARTING_SQUARE_VISIT_FAILURE #======================#
    "StartingSquareVisitException",
]

from chess.system import UpdateException


# ======================# STARTING_SQUARE_VISIT_FAILURE #======================#
class StartingSquareVisitException(UpdateException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    #   RESPONSIBILITIES:
    1.  An error occurred in OccupationService.add_occupant that prevented a successful UpdateResult.
    2.  This error might have occurred in a different OccupationService method that also returns UpdateResults.

    # PARENT:
        *   UpdateException


    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "STARTING_SQUARE_VISIT_FAILURE"
    MSG = "SquareVisit start failed."