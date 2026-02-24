# src/chess/hostage/databse/coreexception/insertion/direct.py

"""
Module: chess.hostage.database.core.exception.insertion.direct
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# APPENDING_HOSTAGE_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
    "AppendingHostageDirectlyIntoItemsFailedException",
]

from chess.hostage import HostageDataListException


# ======================# APPENDING_HOSTAGE_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
class AppendingHostageDirectlyIntoItemsFailedException(HostageDataListException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that appending the hostage directly into self.bag was not in the list after running bag.append.

    # PARENT:
        *   HostageDataListException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "APPENDING_HOSTAGE_DIRECTLY_INTO_ITEMS_ERROR"
    DEFAULT_MESSAGE = (
        "Hostage insertion failed: The manifest was not found in self.bag after "
        "running self.bag.append."
    )