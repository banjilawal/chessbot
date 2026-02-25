# src/chess/hostage/databse/coreexception/catchall.py

"""
Module: chess.hostage.database.core.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.hostage import HostageException
from chess.system import DataServiceException

__all__ = [
    # ======================# HOSTAGE_LIST EXCEPTION #======================#
    "HostageDataListException",
]


# ======================# HOSTAGE_LIST EXCEPTION #======================#
class HostageDataListException(HostageException, DataServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by HostageList methods that return Result objects.

    # PARENT:
        *   HostageException
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "HOSTAGE_LIST_ERROR"
    MSG = "HostageList raised an exception."