# src/logic/hostage/database/kernel/exception/insertion/validator.py

"""
Module: logic.hostage.database.kernel.exception.insertion.work
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_HOSTAGE_INSERTION_FAILURE #======================#
    "UniqueHostageInsertionException",
]

from model.hostage import HostageException
from system import InsertionException


# ======================# UNIQUE_HOSTAGE_INSERTION_FAILURE #======================#
class UniqueHostageInsertionException(HostageException, InsertionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why inserting a unique manifest failed. The encapsulated
        exceptions create  chain for tracing the source of the failure.

    Super Class:
        *   HostageException
        *   InsertionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "UNIQUE_HOSTAGE_INSERTION_FAILURE"
    MSG = "Unique Hostage insertion failed."