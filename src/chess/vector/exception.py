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

#====================== NULL VECTOR EXCEPTIONS #======================#
  "NullVectorException",
  
#====================== VECTOR VALIDATION EXCEPTIONS #======================#
  "InvalidVectorException",

#====================== VECTOR BUILD EXCEPTIONS #======================#  
  "VectorBuildFailedException",

#====================== NULL COMPONENT EXCEPTIONS #======================#  
  "VectorAboveBoundsException",
  "VectorBelowBoundsException",

#====================== VECTOR BOUNDS EXCEPTIONS #======================#  
  "NullXComponentException",
  "NullYComponentException",
]

class VectorException(ChessException):
  """
  Super class of exceptions raised by Scalar objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "VECTOR_ERROR"
  DEFAULT_MESSAGE = "Vector raised an exception."



#====================== NULL VECTOR EXCEPTIONS #======================#















