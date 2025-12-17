# src/chess/schema/validator/exception/base.py

"""
Module: chess.schema.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.schema import SchemaException
from chess.system import ValidationFailedException


__all__ = [
    #======================# SCHEMA_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidSchemaException",
]

#======================# SCHEMA VALIDATION EXCEPTION #======================#
class InvalidSchemaException(SchemaException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by SchemaValidation objects.
    2.  Wraps unhandled exceptions that hit the finally-block in SchemaValidator methods.
    
    # PARENT:
        *   SchemaException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "_SCHEMA_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Schema validation failed."
