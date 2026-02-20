# src/chess/edge/service/exception/update/heuristic.py

"""
Module: chess.edge.service.exception.update.heuristic
Author: Banji Lawal
Created: 2025-02-20
version: 1.0.0
"""

from chess.edge import EdgeException
from chess.system import UpdateFailedException


class UpdatingEdgeHeuristicException(EdgeException, UpdateFailedException):
    pass