# src/chess/schema/map/builder/exception.py

"""
Module: chess.schema.map.builder.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaMapException
from chess.system import BuildFailedException


__all__ = [
    #======================# SCHEMA_CONTEXT BUILD EXCEPTION #======================#
    "SchemaMapBuildFailedException",
]


#======================# SCHEMA_CONTEXT BUILD EXCEPTION #======================#
class SchemaMapBuildFailedException(SchemaMapException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during SchemaMap build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an SchemaMapBuilder method.
    
    # PARENT:
        *   SchemaMapException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "SchemaMap build failed."