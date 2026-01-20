# src/chess/hostage/service/data/unique/exception/insertion/duplicate.py

"""
Module: chess.hostage.service.data.unique.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.hostage import UniqueHostageManifestDataServiceException

__all__ = [
    # ======================# ADDING_DUPLICATE_HOSTAGE_MANIFEST EXCEPTION #======================#
    "AddingDuplicateHostageManifestException",
]


# ======================# ADDING_DUPLICATE_HOSTAGE_MANIFEST EXCEPTION #======================#
class AddingDuplicateHostageManifestException(UniqueHostageManifestDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a item to the UniqueHostageManifestDataService's dataset failed
        because it was already present.

    # PARENT:
        *   UniqueHostageManifestDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_HOSTAGE_MANIFEST_ERROR"
    DEFAULT_MESSAGE = "Unique HostageManifest insertion failed: The manifest was already present."