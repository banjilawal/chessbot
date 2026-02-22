# src/chess/schema/key/builder/exception/wrapper.py

"""
Module: chess.schema.key.builder.exception..wrapper
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import BuildException
from chess.schema import SchemaKeyException



__all__ = [
    # ======================# SCHEMA_KEY_BUILD_FAILURE #======================#
    "SchemaKeyBuildException",
]


#======================# SCHEMA_KEY_BUILD_FAILURE #======================#
class SchemaKeyBuildException(SchemaKeyException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the SchemaKey build creates an exception. Failed check exceptions are encapsulated
        in a SchemaKeyBuildException which is sent to the caller in a BuildResult.
    2.  The SchemaKeyBuildException provides a trace for debugging and application recovery.
        # RESPONSIBILITIES:

    # PARENT:
        *   BuildException
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