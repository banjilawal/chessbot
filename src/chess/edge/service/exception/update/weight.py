# src/chess/edge/service/exception/update/weight.py

"""
Module: chess.edge.service.exception.update.weight
Author: Banji Lawal
Created: 2025-02-20
version: 1.0.0
"""

from chess.edge import EdgeServiceException
from chess.system import UpdateFailedException

__all__ = [
    # ======================# EDGE_WEIGHT_UPDATE_FAILURE #======================#
    "UpdatingEdgeWeightException",
]


# ======================# EDGE_WEIGHT_UPDATE_FAILURE #======================#
class UpdatingEdgeWeightException(EdgeServiceException, UpdateFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why an edge's weight could not be updated. The exception chain
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
    ERROR_CODE = "EDGE_WEIGHT_UPDATE_FAILURE"
    DEFAULT_MESSAGE = "Edge weight update failed."