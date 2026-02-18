# src/chess/graph/square/validator/exception/debug/null.py

"""
Module: chess.graph.square.validator.exception.debug/null
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.graph import EdgeException
from chess.system import NullException


class NullEgeException(EdgeException, NullException):
    pass