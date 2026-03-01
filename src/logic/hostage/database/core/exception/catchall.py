# src/logic/hostage/databse/coreexception/super.py

"""
Module: logic.hostage.database.core.exception.super
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from logic.hostage import HostageException
from logic.system import DataServiceException

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
    ERR_CODE = "HOSTAGE_LIST_EXCEPTION"
    MSG = "HostageList raised an exception."