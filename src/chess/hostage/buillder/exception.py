# src/chess/hostage/builder/exception.py

"""
Module: chess.hostage.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.hostage import HostageManifestException
from chess.system import BuildFailedException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_BUILD_FAILURE EXCEPTION #======================#
    "HostageManifestBuildFailedException",
]


# ======================# HOSTAGE_MANIFEST_BUILD_FAILURE EXCEPTION #======================#
class HostageManifestBuildFailedException(HostageManifestException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the HostageManifest build creates an exception. Failed check exceptions are 
        encapsulated in an HostageManifestBuildFailedException which is sent to the caller in a BuildResult.
    2.  The HostageManifestBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   HostageManifestException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_BUILD_FAILURE"
    DEFAULT_MESSAGE = "HostageManifest build failed."