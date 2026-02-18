# src/chess/graph/square/validator/exception/debug/distance.py

"""
Module: chess.graph.square.validator.exception.debug/distance
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""


from chess.graph import EdgeException
from chess.system import DebugException


class EdgeDistanceException(EdgeException, DebugException):
    pass