# src/chess/schema/key/builder/exception/wrapper.py

"""
Module: chess.schema.key.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.schema import SchemaSuperKeyException



__all__ = [
    # ======================# SCHEMA_SUPER_KEY_BUILD_FAILED EXCEPTION #======================#
    "SchemaSuperKeyBuildFailedException",
]


#======================# SCHEMA_SUPER_KEY_BUILD_FAILED EXCEPTION #======================#
class SchemaSuperKeyBuildFailedException(SchemaSuperKeyException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Messaging, Data Transport.

    # RESPONSIBILITIES:
    1.  If an error occurs during the SchemaSuperKey build process it raises an exception. The exception is
        encapsulated in a SchemaSuperKeyBuildFailedException.
    2.  The SchemaSuperKeyBuildFailed is sent to the caller in a BuildResult providing the caller an exception
        chain for tracing the failure to its ultimate source.
    
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
    ERROR_CODE = "SCHEMA_SUPER_KEY_BUILD_FAILED"
    DEFAULT_MESSAGE = "SchemaSuperKey build failed:"