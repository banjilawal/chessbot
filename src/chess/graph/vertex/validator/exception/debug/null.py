# src/chess/graph/vertex/validator/exception/debug/null.py

"""
Module: chess.graph.vertex.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.graph import VertexException
from chess.system import NullException


class NullVertexException(VertexException, NullException):
    pass