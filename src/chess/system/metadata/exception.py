# src/chess/system/metadata/exception.py

"""
Module: chess.system.metadata.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# METADATA EXCEPTION #======================#
    "MetadataException",
]


# ======================# METADATA EXCEPTION #======================#
class MetadataException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Metadata objects
    3.  Catchall for Metadata failure states that are not covered by a lower level Metadata exception.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    MetadataException
  
    # LOCAL ATTRIBUTES:
    None
  
    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "METADATA_ERROR"
    DEFAULT_MESSAGE = "Metadata raised an exception."