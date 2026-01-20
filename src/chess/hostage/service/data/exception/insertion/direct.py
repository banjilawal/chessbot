# src/chess/hostage/service/data/exception/insertion/direct.py

"""
Module: chess.hostage.service.data.exception.insertion.direct
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# APPENDING_HOSTAGE_MANIFEST_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
    "AppendingHostageManifestDirectlyIntoItemsFailedException",
]

from chess.hostage import HostageManifestDataListException


# ======================# APPENDING_HOSTAGE_MANIFEST_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
class AppendingHostageManifestDirectlyIntoItemsFailedException(HostageManifestDataListException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that appending the hostageManifest directly into self.items was not in the list after running items.append.

    # PARENT:
        *   HostageManifestDataListException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "APPENDING_HOSTAGE_MANIFEST_DIRECTLY_INTO_ITEMS_ERROR"
    DEFAULT_MESSAGE = (
        "HostageManifest insertion failed: The manifest was not found in self.items after "
        "running self.items.append."
    )