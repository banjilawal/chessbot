# src/chess/schema/map/builder/exception.py

"""
Module: chess.schema.map.builder.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKeyException
from chess.system import BuildFailedException


__all__ = [
    #======================# SCHEMA_SUPER_KEY BUILD EXCEPTION #======================#
    "SchemaSuperKeyBuildFailedException",
]


#======================# SCHEMA_SUPER_KEY BUILD EXCEPTION #======================#
class SchemaSuperKeyBuildFailedException(SchemaSuperKeyException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during SchemaSuperKey build process.
    2.  Wraps exceptions that hit the try-finally block of an SchemaMapBuilder method.
    
    # PARENT:
        *   SchemaSuperKeyException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_SUPER_KEY_BUILD_ERROR"
    DEFAULT_MESSAGE = "SchemaSuperKey build failed."