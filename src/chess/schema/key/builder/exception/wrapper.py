# src/chess/schema/key/builder/exception/wrapper.py

"""
Module: chess.schema.key.builder.exception..wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.schema import SchemaKeyException



__all__ = [
    # ======================# SCHEMA_KEY_BUILD_FAILED EXCEPTION #======================#
    "SchemaKeyBuildFailedException",
]


#======================# SCHEMA_KEY_BUILD_FAILED EXCEPTION #======================#
class SchemaKeyBuildFailedException(SchemaKeyException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the SchemaKey build creates an exception. Failed check exceptions are encapsulated
        in a SchemaKeyBuildFailedException which is sent to the caller in a BuildResult.
    2.  The SchemaKeyBuildFailedException provides a trace for debugging and application recovery.
        # RESPONSIBILITIES:

    # PARENT:
        *   BuildFailedException
        *   SchemaKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_KEY_BUILD_FAILED"
    DEFAULT_MESSAGE = "SchemaKey build failed:"