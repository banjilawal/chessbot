# src/chess/schema/key/builder/exception/wrapper.py

"""
Module: chess.schema.key.builder.exception..wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.schema import SchemaSuperKeyException



__all__ = [
    # ======================# SCHEMA_KEY_BUILD_FAILED EXCEPTION #======================#
    "SchemaSuperKeyBuildFailedException",
]


#======================# SCHEMA_KEY_BUILD_FAILED EXCEPTION #======================#
class SchemaSuperKeyBuildFailedException(SchemaSuperKeyException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the SchemaSuperKey build creates an exception. Failed check exceptions are encapsulated
        in a SchemaSuperKeyBuildFailedException which is sent to the caller in a BuildResult.
    2.  The SchemaSuperKeyBuildFailedException provides a trace for debugging and application recovery.
        # RESPONSIBILITIES:

    # PARENT:
        *   BuildFailedException
        *   SchemaSuperKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_KEY_BUILD_FAILED"
    DEFAULT_MESSAGE = "SchemaSuperKey build failed:"