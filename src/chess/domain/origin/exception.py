# src/chess/points/origin/exception.py

"""
Module: chess.points.origin.exception
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""

from chess.system import (
    ChessException, NullException, ValidationException, BuildException, InconsistencyException
)

__all__ = [
    "DomainOriginException",
    
#====================== NULL DOMAIN_ORIGIN EXCEPTION #======================#
    "NullDomainOriginException",


#====================== DOMAIN_ORIGIN VALIDATION EXCEPTION #======================#
    "InvalidDomainOriginException",
    
    #====================== DOMAIN_ORIGIN BUILD EXCEPTION #======================#
    "DomainOriginBuildException",
]


class DomainOriginException(ChessException):
    """
    Super class of exception raised by DomainOrigin objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERR_CODE = "DOMAIN_ORIGIN_ERROR"
    MSG = "An rollback_exception was raised by a DomainOrigin."


#====================== NULL DOMAIN_ORIGIN EXCEPTION #======================#
class NullDomainOriginException(DomainOriginException, NullException):
    """Raised if an entity, method, or operation requires DomainOrigin but gets null instead."""
    ERR_CODE = "NULL_DOMAIN_ORIGIN_ERROR"
    MSG = "A DomainOrigin cannot be null."


#====================== DOMAIN_ORIGIN VALIDATION EXCEPTION #======================#
class InvalidDomainOriginException(DomainOriginException, ValidationException):
    """Catchall Exception for DomainOriginValidator when a candidate fails a sanity check.""""""
    ERR_CODE = "DOMAIN_ORIGIN_VALIDATION_ERROR"
    MSG = "DomainOrigin validation failed."


#====================== DOMAIN_ORIGIN BUILD EXCEPTION #======================#
class DomainOriginBuildException(DomainOriginException, BuildException):
    """Catchall Exception for DomainOriginBuilder when it stops because of an error."""
    ERR_CODE = "DOMAIN_ORIGIN_BUILD_FAILED"
    MSG = "DomainOrigin build failed."