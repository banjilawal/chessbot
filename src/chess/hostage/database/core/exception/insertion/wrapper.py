# src/chess/hostage/databse/coreexception/insertion/wrapper.py

"""
Module: chess.hostage.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# HOSTAGE_MANIFEST_INSERTION_FAILURE #======================#
    "HostageManifestInsertionException",
]

from chess.hostage import HostageManifestException
from chess.system import InsertionException


# ======================# HOSTAGE_MANIFEST_INSERTION_FAILURE #======================#
class HostageManifestInsertionException(HostageManifestException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that add a hostageManifest to the dataset failed.

    # PARENT:
        *   HostageManifestException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "HostageManifest insertion failed."