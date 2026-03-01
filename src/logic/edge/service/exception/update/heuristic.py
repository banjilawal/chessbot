# src/logic/edge/service/exception/update/heuristic.py

"""
Module: logic.edge.service.exception.update.heuristic
Author: Banji Lawal
Created: 2025-02-20
version: 1.0.0
"""

from logic.edge import EdgeServiceException
from logic.system import UpdateException

__all__ = [
    # ======================# EDGE_HEURISTIC_UPDATE_FAILURE #======================#
    "UpdatingEdgeHeuristicException",
]


# ======================# EDGE_HEURISTIC_UPDATE_FAILURE #======================#
class UpdatingEdgeHeuristicException(EdgeServiceException, UpdateException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why an edge's heuristic could not be updated. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   EdgeServiceException
        *   UpdateException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "EDGE_HEURISTIC_UPDATE_FAILURE"
    MSG = "Edge heuristic update failed."