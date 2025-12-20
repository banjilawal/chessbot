# src/chess/vector/collision.py

"""
Module: chess.vector.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException, BuildFailedException


__all__ = [
  "VectorException",

#====================== NULL VECTOR EXCEPTION #======================#
  "NullVectorException",
  
#====================== VECTOR VALIDATION EXCEPTION #======================#
  "InvalidVectorException",

#====================== VECTOR BUILD EXCEPTION #======================#
  "VectorBuildFailedException",

#====================== NULL COMPONENT EXCEPTION #======================#
  "VectorAboveBoundsException",
  "VectorBelowBoundsException",

#====================== VECTOR BOUNDS EXCEPTION #======================#
  "NullXComponentException",
  "NullYComponentException",
]

class VectorException(ChessException):
  """
  Super class of exception raised by Scalar objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "VECTOR_ERROR"
  DEFAULT_MESSAGE = "Vector raised an exception."



#====================== NULL VECTOR EXCEPTION #======================#















