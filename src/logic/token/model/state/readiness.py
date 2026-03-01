# src/logic/token/model/state/readiness.py

"""
Module: logic.token.model.state.readiness
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto

class ReadinessState(Enum):
    """
    # ROLE: State Descriptor

    # RESPONSIBILITIES:
    1.  Indicating if the Token is in a state where
            *   It has not been formed on the board.
            *   It can move on board.
            *   It can capture enemies.  
            *   It cannot move on the board nor capture enemies.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   FREE
        *   IN_CHECK
        *   CHECKMATED
        *   NOT_INITIALIZED
        *   CAPTURE_ACTIVATED
        *   HOSTAGE_CREATED
        *   HOSTAGE_IN_DATABASE
        *   DEACTIVATED`

    # INHERITED ATTRIBUTES:
        *   See Enum class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
   None

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See Enum class for inherited methods.
    """
    FREE = auto(),
    IN_CHECK = auto(),
    CHECKMATED = auto(),
    NOT_INITIALIZED = auto(),
    CAPTURE_ACTIVATED = auto(),
    HOSTAGE_CREATED = auto(),
    HOSTAGE_IN_DATABASE = auto(),
    DEACTIVATED = auto(),