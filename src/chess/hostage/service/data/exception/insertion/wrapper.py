# src/chess/hostage/service/data/exception/insertion/wrapper.py

"""
Module: chess.hostage.service.data.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# HOSTAGE_MANIFEST_INSERTION_FAILURE #======================#
    "HostageManifestInsertionFailedException",
]

from chess.hostage import HostageManifestException
from chess.system import InsertionFailedException


# ======================# HOSTAGE_MANIFEST_INSERTION_FAILURE #======================#
class HostageManifestInsertionFailedException(HostageManifestException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that add a hostageManifest to the dataset failed.

    # PARENT:
        *   HostageManifestException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_INSERTION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "HostageManifest insertion failed."