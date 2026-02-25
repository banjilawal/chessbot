# src/chess/vector/service/exception/wrapper.py

"""
Module: chess.vector.service.exception.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
  "VectorServiceException",
  
#======================# VECTOR_SERVICE VALIDATION EXCEPTION #======================#
]

from chess.system import ServiceException
from chess.vector import VectorException


# ======================# VECTOR_SERVICE EXCEPTION #======================#
class VectorServiceException(VectorException, ServiceException):
  """
  Super class of exception raised by VectorService objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERR_CODE = "VECTOR_SERVICE_ERROR"
  MSG = "VectorService operation failed."
