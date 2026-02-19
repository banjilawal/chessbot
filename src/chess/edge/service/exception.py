# src/chess/edge/service/exception.py

"""
Module: chess.edge.service.exception
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.edge import EdgeException
from chess.system import EntityServiceException

__all__ = [
    # ======================# EDGE_SERVICE EXCEPTION #======================#
    "EdgeServiceException",
]

class EdgeServiceException(EdgeException, EntityServiceException):
    pass