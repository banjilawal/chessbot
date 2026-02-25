# src/chess/hostage/context/exception.py

"""
Module: chess.hostage.context.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.hostage import HostageException
from chess.system import ContextException

__all__ = [
    # ======================# HOSTAGE_CONTEXT EXCEPTION #======================#
    "CaptivityContextException",
]


# ======================# HOSTAGE_CONTEXT EXCEPTION #======================#
class CaptivityContextException(HostageException, ContextException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CaptivityContext objects.

    # PARENT:
        *   HostageException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "HOSTAGE_CONTEXT_ERROR"
    DEFAULT_ERR_CODE = "CaptivityContext raised an exception."