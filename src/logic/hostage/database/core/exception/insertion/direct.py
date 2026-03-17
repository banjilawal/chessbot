# src/logic/hostage/databse/coreexception/insertion/direct.py

"""
Module: logic.hostage.database.core.exception.insertion.direct
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# APPENDING_HOSTAGE_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
    "AppendingHostageDirectlyIntoItemsFailedException",
]

from logic.hostage import HostageDataListException


# ======================# APPENDING_HOSTAGE_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
class AppendingHostageDirectlyIntoItemsFailedException(HostageDataListException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that appending the hostage directly into self.bag was not in the list after running bag.append.

    Super Class:
        *   HostageDataListException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "APPENDING_HOSTAGE_DIRECTLY_INTO_ITEMS_EXCEPTION"
    MSG = (
        "Hostage insertion failed: The manifest was not found in self.bag after "
        "running self.bag.append."
    )