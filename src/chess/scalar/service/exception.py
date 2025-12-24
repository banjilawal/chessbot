# src/chess/scalar/service/exception.py

"""
Module: chess.scalar.service.exception
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from chess.system import ServiceException, NullException, ValidationException, BuildFailedException

__all__ = [
  "ScalarServiceException",
  
#======================# SCALARSERVICE VALIDATION EXCEPTION #======================#
  "NullScalarServiceException",
  "InvalidScalarServiceException",
  
#======================# SCALARSERVICE BUILD EXCEPTION #======================#
  "ScalarBuildFailedException",
]

class ScalarServiceException(ServiceException):
  """
  Super class of exception raised by ScalarService objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "SCALAR_SERVICE_ERROR"
  DEFAULT_MESSAGE = "ScalarService raised an exception."
  

#======================# NULL SCALARSERVICE EXCEPTION #======================#
class NullScalarServiceException(ScalarServiceException, NullException):
  """Raised if an entity, method, or operation requires ScalarService but gets null instead."""
  ERROR_CODE = "NULL_SCALAR_SERVICE_ERROR"
  DEFAULT_MESSAGE = "ScalarService cannot be null."


#======================# SCALARSERVICE VALIDATION EXCEPTION #======================#
class InvalidScalarServiceException(ScalarServiceException, ValidationException):
  """Catchall Exception for ScalarValidator when a candidate fails a sanity check."""
  ERROR_CODE = "SCALAR_SERVICE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "ScalarService validation failed."


#======================# SCALARSERVICE BUILD EXCEPTION #======================#
class ScalarBuildFailedException(ScalarServiceException, BuildFailedException):
  """Catchall Exception for ScalarServiceBuilder when it encounters an error building a ScalarService."""
  ERROR_CODE = "SCALAR_SERVICE_BUILD_FAILED"
  DEFAULT_MESSAGE = "ScalarService build failed."
