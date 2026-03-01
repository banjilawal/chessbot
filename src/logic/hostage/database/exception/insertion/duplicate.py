# src/logic/hostage/database/exception/insertion/duplicate.py

"""
Module: logic.hostage.database.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from logic.hostage import HostageDatabase

__all__ = [
    # ======================# ADDING_DUPLICATE_HOSTAGE EXCEPTION #======================#
    "AddingDuplicateHostageException",
]


# ======================# ADDING_DUPLICATE_HOSTAGE EXCEPTION #======================#
class AddingDuplicateHostageException(HostageDatabase):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a item to the HostageDatabase's dataset failed
        because it was already present.

    # PARENT:
        *   HostageDatabase

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_HOSTAGE_EXCEPTION"
    MSG = "Unique Hostage insertion failed: The manifest was already present."