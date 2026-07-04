# src/model/state/token/state/activity.py

"""
Module: model.state.token.state.activity
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class TokenActivityState(Enum):
    """
    Role:
        -   State
    
    Responsibilities:
        1.  Describes Token activity states
    
    Attributes:
    
    Provides:
    
    Super Class:
        Enum
    """
    FREE = auto(),
    IN_CHECK = auto(),
    CHECKMATED = auto(),
    NOT_INITIALIZED = auto(),
    CAPTURE_ACTIVATED = auto(),
    HOSTAGE_CREATED = auto(),
    HOSTAGE_IN_DATABASE = auto(),
    DEACTIVATED = auto(),