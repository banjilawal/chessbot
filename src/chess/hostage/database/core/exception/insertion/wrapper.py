# src/chess/hostage/databse/coreexception/insertion/wrapper.py

"""
Module: chess.hostage.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# HOSTAGE_INSERTION_FAILURE #======================#
    "HostageInsertionException",
]

from chess.hostage import HostageException
from chess.system import InsertionException


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
    ERROR_CODE = "HOSTAGE_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Hostage insertion failed."