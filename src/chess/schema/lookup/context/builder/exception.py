# src/chess/schema/lookup/context/builder/exception.py

"""
Module: chess.schema.lookup.context.builder.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaContextException
from chess.system import BuildFailedException


__all__ = [
    #======================# SCHEMA_CONTEXT BUILD EXCEPTIONS #======================#
    "SchemaContextBuildFailedException",
]


#======================# SCHEMA_CONTEXT BUILD EXCEPTIONS #======================#
class SchemaContextBuildFailedException(SchemaContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during SchemaContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an SchemaContextBuilder method.
    
    # PARENT:
        *   SchemaContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "SchemaContext build failed."