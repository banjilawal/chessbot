# src/chess/scalar/service/exception.py

"""
Module: chess.scalar.service.exception
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from chess.system import ServiceException, NullException, ValidationException, BuildException

__all__ = [
  "ScalarServiceException",
  
#======================# SCALARSERVICE VALIDATION EXCEPTION #======================#
  "NullScalarServiceException",
  "InvalidScalarServiceException",
  
#======================# SCALARSERVICE BUILD EXCEPTION #======================#
    "ScalarBuildException",
]

class ScalarServiceException(ServiceException):
  """
  Super class of exception raised by ScalarService objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERR_CODE = "SCALAR_SERVICE_ERROR"
  MSG = "ScalarService raised an exception."
  

#======================# NULL SCALARSERVICE EXCEPTION #======================#
class NullScalarServiceException(ScalarServiceException, NullException):
  """Raised if an entity, method, or operation requires ScalarService but gets null instead."""
  ERR_CODE = "NULL_SCALAR_SERVICE_ERROR"
  MSG = "ScalarService cannot be null."


#======================# SCALARSERVICE VALIDATION EXCEPTION #======================#
class InvalidScalarServiceException(ScalarServiceException, ValidationException):
  """Catchall Exception for ScalarValidator when a candidate fails a sanity check."""
  ERR_CODE = "SCALAR_SERVICE_VALIDATION_ERROR"
  MSG = "ScalarService validation failed."


#======================# SCALARSERVICE BUILD EXCEPTION #======================#
class ScalarBuildException(ScalarServiceException, BuildException):
  """Catchall Exception for ScalarServiceBuilder when it encounters an error building a ScalarService."""
  ERR_CODE = "SCALAR_SERVICE_BUILD_FAILED"
  MSG = "ScalarService build failed."
