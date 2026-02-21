# src/chess/edge/service/exception/update/heuristic.py

"""
Module: chess.edge.service.exception.update.heuristic
Author: Banji Lawal
Created: 2025-02-20
version: 1.0.0
"""

from chess.edge import EdgeServiceException
from chess.system import UpdateFailedException

__all__ = [
    # ======================# EDGE_HEURISTIC_UPDATE_FAILURE #======================#
    "UpdatingEdgeHeuristicException",
]


# ======================# EDGE_HEURISTIC_UPDATE_FAILURE #======================#
class UpdatingEdgeHeuristicException(EdgeServiceException, UpdateFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why an edge's heuristic could not be updated. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   EdgeServiceException
        *   UpdateFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_HEURISTIC_UPDATE_FAILURE"
    DEFAULT_MESSAGE = "Edge heuristic update failed."