# src/model/square/state.py

"""
Module: model.square.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto


class SquareState(Enum):
    """
    Role:
        -   State Descriptor

    Responsibilities:
        1.  Indicates if the square can be visited.
        
    Provides

    Super Class:
        Enum
    """
    EMPTY = auto(),
    OCCUPIED = auto(),