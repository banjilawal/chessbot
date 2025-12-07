# src/chess/system/builder/exception/certification.py

"""
Module: chess.system.builder.exception.certification
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuilderException, NullException

__all__ = [
    # ======================# UNRELIABLE_BUILDER_EXCEPTION #======================#
    "UnreliableBuilderException",
    # ======================# NULL_BUILDER_EXCEPTION #======================#
    "NullBuilderException",
]


# ======================# UNRELIABLE_BUILDER_EXCEPTION #======================#
class UnreliableBuilderException(BuilderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
  
    # RESPONSIBILITIES:
    Catchall for when Builder certification check hits the try-finally block with an unhandled exception.
    
    # PARENT
        *   BuilderException
        *   ValidationFailedException
  
    # PROVIDES:
    UnreliableBuilderException
  
    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "BUILDER_CERTIFICATION_ERROR"
    DEFAULT_MESSAGE = "Builder certification failed. Do not rely on this builder."


# ======================# NULL_BUILDER_EXCEPTION #======================#
class NullBuilderException(UnreliableBuilderException, NullException):
    """
    # ROLE: Error Tracing, Debugging
  
    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required aBuilder but got null instead.
  
    # PARENT
        *   InvalidBuilderException
        *   NullException
  
    # PROVIDES:
    NullBuilderException
  
    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_BUILDER_ERROR"
    DEFAULT_MESSAGE = "Builder cannot be null."
