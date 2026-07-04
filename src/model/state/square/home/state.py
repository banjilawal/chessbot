# src/model/state/square/home/state.py

"""
Module: model.state.square.home/state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class TokenHomeClaimState(Enum):
    """
    Role:
        -   State Descriptor

    Responsibilities:
        1.  Indicates if the square can be visited.
        
    Provides

    Super Class:
        Enum
    """
    UNCLAIMED = auto(),
    CLAIMED = auto(),