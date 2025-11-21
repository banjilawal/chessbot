# src/chess/domain/origin/collision.py

"""
Module: chess.domain.origin.exception
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""

from chess.system import (
    ChessException, NullException, ValidationException, BuildFailedException, InconsistencyException
)

__all__ = [
    "DomainOriginException",
    
#====================== NULL DOMAIN_ORIGIN EXCEPTIONS #======================#
    "NullDomainOriginException",


#====================== DOMAIN_ORIGIN VALIDATION EXCEPTIONS #======================#
    "InvalidDomainOriginException",
    
    # ====================== DOMAIN_ORIGIN BUILD EXCEPTIONS #======================#
    "DomainOriginBuildFailedException",
]


class DomainOriginException(ChessException):
    """
    Super class of exceptions raised by DomainOrigin objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "DOMAIN_ORIGIN_ERROR"
    DEFAULT_MESSAGE = "An rollback_exception was raised by a DomainOrigin."


# ====================== NULL DOMAIN_ORIGIN EXCEPTIONS #======================#
class NullDomainOriginException(DomainOriginException, NullException):
    """Raised if an entity, method, or operation requires DomainOrigin but gets validation instead."""
    ERROR_CODE = "NULL_DOMAIN_ORIGIN_ERROR"
    DEFAULT_MESSAGE = "A DomainOrigin cannot be validation."


# ====================== DOMAIN_ORIGIN VALIDATION EXCEPTIONS #======================#
class InvalidDomainOriginException(DomainOriginException, ValidationException):
    """Catchall Exception for DomainOriginValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "DOMAIN_ORIGIN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "DomainOrigin validation failed."


# ====================== DOMAIN_ORIGIN BUILD EXCEPTIONS #======================#
class DomainOriginBuildFailedException(DomainOriginException, BuildFailedException):
    """Catchall Exception for DomainOriginBuilder when it stops because of an error."""
    ERROR_CODE = "DOMAIN_ORIGIN_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "DomainOrigin build failed."