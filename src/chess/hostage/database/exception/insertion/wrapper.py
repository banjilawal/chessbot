# src/chess/hostageManifest/service/data/exception/insertion/wrapper.py

"""
Module: chess.hostageManifest.service.data.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_HOSTAGE_MANIFEST_INSERTION_FAILURE EXCEPTION #======================#
    "UniqueHostageManifestInsertionFailedException",
]

from chess.hostage import HostageManifestException
from chess.system import InsertionFailedException


# ======================# UNIQUE_HOSTAGE_MANIFEST_INSERTION_FAILURE EXCEPTION #======================#
class UniqueHostageManifestInsertionFailedException(HostageManifestException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting a unique manifest failed. The encapsulated
        exceptions create  chain for tracing the source of the failure.

    # PARENT:
        *   HostageManifestException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_HOSTAGE_MANIFEST_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Unique HostageManifest insertion failed."