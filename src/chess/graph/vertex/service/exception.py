# src/chess/graph/node/service/exception.py

"""
Module: chess.graph.node.service.exception
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.graph import NodeException
from chess.system import EntityServiceException

__all__ = [
    # ======================# NODE_SERVICE EXCEPTION #======================#
    "NodeServiceException",
]

class NodeServiceException(NodeException, EntityServiceException):
    pass