# src/chess/vector/service/collision.py

"""
Module: chess.vector.service.exception
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from chess.system import ServiceException, NullException, ValidationException, BuildFailedException

__all__ = [
  "VectorServiceException",
  
#======================# VECTOR_SERVICE VALIDATION EXCEPTIONS #======================#  
  "NullVectorServiceException",
  "InvalidVectorServiceException",
  
#======================# VECTOR_SERVICE BUILD EXCEPTIONS #======================#  
  "VectorBuildFailedException",
]

class VectorServiceException(ServiceException):
  """
  Super class of exceptions raised by VectorService objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "VECTOR_SERVICE_ERROR"
  DEFAULT_MESSAGE = "VectorService raised an exception."
  

#======================# NULL VECTOR_SERVICE EXCEPTIONS #======================#
class NullVectorServiceException(VectorServiceException, NullException):
  """Raised if an entity, method, or operation requires VectorService but gets validation instead."""
  ERROR_CODE = "NULL_VECTOR_SERVICE_ERROR"
  DEFAULT_MESSAGE = "VectorService cannot be validation."


#======================# VECTOR_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidVectorServiceException(VectorServiceException, ValidationException):
  """Catchall Exception for VectorValidator when a validation candidate fails a sanity check."""
  ERROR_CODE = "VECTOR_SERVICE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "VectorService validation failed."


#======================# VECTOR_SERVICE BUILD EXCEPTIONS #======================#
class VectorBuildFailedException(VectorServiceException, BuildFailedException):
  """Catchall Exception for VectorServiceBuilder when it encounters an error building a VectorService."""
  ERROR_CODE = "VECTOR_SERVICE_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "VectorService build failed."
