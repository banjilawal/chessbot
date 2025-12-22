# src/chess/schema/key/builder/exception.py

"""
Module: chess.schema.key.builder.exception
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
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an error prevented the SchemaSuperKey build from completing successfully.
    2.  Wrap an exception that hit the try-finally block of a SchemSuperKeyBuilder method.
    
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
    ERROR_CODE = "SCHEMA_SUPER_KEY_BUILD_ERROR"
    DEFAULT_MESSAGE = "SchemaSuperKey build failed."