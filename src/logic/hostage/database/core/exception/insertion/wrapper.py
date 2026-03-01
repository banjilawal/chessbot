# src/logic/hostage/databse/coreexception/insertion/wrapper.py

"""
Module: logic.hostage.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# HOSTAGE_INSERTION_FAILURE #======================#
    "HostageInsertionException",
]

from logic.hostage import HostageException
from logic.system import InsertionException


# ======================# HOSTAGE_INSERTION_FAILURE #======================#
class HostageInsertionException(HostageException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that add a hostage to the dataset failed.

    # PARENT:
        *   HostageException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "HOSTAGE_INSERTION_FAILURE"
    MSG = "Hostage insertion failed."