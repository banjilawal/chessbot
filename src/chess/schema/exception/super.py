# src/chess/schema/exception.py

"""
Module: chess.schema.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# SCHEMA EXCEPTION #======================#
    "SchemaException",
]

from chess.system import SuperClassException


# ======================# SCHEMA EXCEPTION #======================#
class SchemaException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of SchemaDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERROR_CODE = "SCHEMA_ERROR"
    DEFAULT_MESSAGE = "Schema raised an exception."