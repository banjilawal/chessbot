# src/chess/points/exception.py

"""
Module: chess.points.exception
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from chess.system import (
    ChessException, BuilderException, InconsistencyException, NullException, ValidationException
)

__all__ = [
    "DomainException",
    
#======================# NULL DOMAIN EXCEPTION #======================#
    "NullDomainException",
    
#======================# DOMAIN VALIDATION EXCEPTION #======================#
    "InvalidDomainException",
    "DomainNullSquaresListException",
    "DomainNullEnemiesDictException",
    "DomainNullFriendsDictException",
    
#======================# DOMAIN BUILD EXCEPTION #======================#
    "DomainBuildException",
]


class DomainException(ChessException):
    """
    Super class of exception raised by Domain objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERR_CODE = "DOMAIN_ERROR"
    MSG = "Domain raised an exception."


#======================# NULL DOMAIN EXCEPTION #======================#
class NullDomainException(DomainException, NullException):
    """Raised if an entity, method, or operation requires Domain but gets null instead."""
    ERR_CODE = "NULL_DOMAIN_ERROR"
    MSG = "Domain cannot be null."


#======================# DOMAIN VALIDATION EXCEPTION #======================#
class InvalidDomainException(DomainException, ValidationException):
    """Super Exception for SquareValidator when a candidate fails a sanity check.""""""
    ERR_CODE = "DOMAIN_VALIDATION_ERROR"
    MSG = "Domain validation failed."


class DomainNullSquaresListException(DomainException, InconsistencyException):
    """"Raised if a Domain's Squares list does not exist."""
    ERR_CODE = "MISSING_SQUARES_LIST_ERROR"
    MSG = "The Domain.squares list is validation. There may be a entity_service failure or data inconsistency."


class DomainNullEnemiesDictException(DomainException, InconsistencyException):
    """Raised if a Domain's enemies dictionary does not exist."""
    ERR_CODE = "MISSING_ENEMY_DICTIONARY_ERROR"
    MSG = "The Domain.enemies dict is validation. There may be a entity_service failure or data inconsistency."


class DomainNullFriendsDictException(DomainException, InconsistencyException):
    """Raised if a Domain's friends dictionary does not exist."""
    ERR_CODE = "MISSING_FRIEND_DICTIONARY_ERROR"
    MSG = "The Domain.friends dict is validation. There may be a entity_service failure or data inconsistency."


#======================# DOMAIN BUILD EXCEPTION #======================#
class DomainBuildException(DomainException, BuilderException):
    """Super Exception for DomainBuilder when it stops because of an error."""
    ERR_CODE = "DOMAIN_BUILD_FAILED"
    MSG = "Domain build failed."
